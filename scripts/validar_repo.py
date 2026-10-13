"""Verificar el paquete portable sin consultas, instalaciones ni escrituras."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

EXCLUDED = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".worktrees"}
PRIVATE_DIRS = {"data", "output", "outputs", "reports", "notebooks", "local", "tmp"}
PRIVATE_SUFFIXES = {".csv", ".parquet", ".feather", ".xls", ".xlsx", ".pkl",
                    ".pickle", ".joblib", ".ipynb", ".log", ".sqlite", ".db",
                    ".pem", ".key", ".pfx", ".p12"}
TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".toml", ".txt"}
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
ABSOLUTE_WINDOWS = re.compile(r"(?<![A-Za-z0-9+.-])[A-Za-z]:[\\/]|\\\\[A-Za-z0-9]")
TOKEN = re.compile(r"\b(?:ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{30,})\b")
PRIVATE_KEY = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def problem(errors: list[str], path: str, message: str) -> None:
    errors.append(f"{path}: {message}")


def local_target(root: Path, owner: Path, target: str) -> tuple[Path | None, str | None]:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    parsed = urlsplit(target)
    if parsed.scheme in {"http", "https", "mailto"}:
        return None, None
    if parsed.scheme or parsed.netloc:
        return None, "URI o ruta local no portable"
    decoded = unquote(parsed.path)
    if not decoded:
        return None, None
    if decoded.startswith(("/", "\\")) or ABSOLUTE_WINDOWS.search(decoded):
        return None, "ruta absoluta no portable"
    resolved = (owner.parent / decoded).resolve()
    if not resolved.is_relative_to(root):
        return None, "la referencia sale del repositorio"
    if not resolved.exists():
        return None, "referencia local inexistente"
    return resolved, None


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("falta frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("frontmatter sin cierre") from exc
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator or key in fields:
            raise ValueError("frontmatter inválido o clave duplicada")
        value = value.strip()
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError as exc:
                raise ValueError("valor citado inválido") from exc
        fields[key] = value
    return fields


def validate_repository(root: Path) -> dict:
    root = root.resolve()
    errors: list[str] = []
    files: list[Path] = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in EXCLUDED for part in rel.parts):
            continue
        if path.is_symlink():
            problem(errors, rel.as_posix(), "enlace simbólico: revisar portabilidad y destino")
            continue
        if not path.is_file():
            continue
        files.append(path)
        name = rel.as_posix()
        if rel.parts[0] in PRIVATE_DIRS or path.suffix.lower() in PRIVATE_SUFFIXES:
            problem(errors, name, "archivo de datos, salida o secreto fuera del paquete")
        if path.name.startswith(".env") and path.name != ".env.example":
            problem(errors, name, "configuración de entorno privada")
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (UnicodeError, OSError):
            problem(errors, name, "texto no legible como UTF-8")
            continue
        if ABSOLUTE_WINDOWS.search(text):
            problem(errors, name, "contiene ruta absoluta de Windows o UNC")
        if TOKEN.search(text) or PRIVATE_KEY.search(text):
            problem(errors, name, "posible credencial o clave privada")
        if path.suffix.lower() == ".md":
            limit = 200 if path.name == "AGENTS.md" else 300
            if len(text.splitlines()) > limit:
                problem(errors, name, f"supera el presupuesto de {limit} líneas")
            for match in LINK.finditer(text):
                _, error = local_target(root, path, match.group(1))
                if error:
                    problem(errors, name, f"{error}: {match.group(1)}")
    for required in ("AGENTS.md", "README.md", ".gitignore", "harness.json"):
        if not (root / required).is_file():
            problem(errors, required, "archivo requerido ausente")

    manifest: dict = {}
    try:
        manifest = json.loads((root / "harness.json").read_text(encoding="utf-8"))
        if not isinstance(manifest, dict):
            raise ValueError("el manifiesto debe ser un objeto")
        if manifest.get("schema_version") != 1 or manifest.get("name") != "data-science-harness":
            problem(errors, "harness.json", "identidad o versión de esquema inválida")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
            problem(errors, "harness.json", "versión de paquete inválida")
    except (OSError, ValueError, TypeError) as exc:
        problem(errors, "harness.json", f"manifiesto no válido: {exc}")
        manifest = {}

    catalog = manifest.get("skills", [])
    if not isinstance(catalog, list):
        problem(errors, "harness.json", "skills debe ser una lista")
        catalog = []
    seen: set[str] = set()
    declared: set[str] = set()
    for skill in catalog:
        if not isinstance(skill, dict):
            problem(errors, "harness.json", "entrada de skill inválida")
            continue
        skill_id = skill.get("id", "")
        if not isinstance(skill_id, str) or not SKILL_NAME.fullmatch(skill_id) or len(skill_id) > 64:
            problem(errors, "harness.json", "id de skill inválido")
            continue
        if skill_id in seen:
            problem(errors, "harness.json", f"skill duplicada: {skill_id}")
        seen.add(skill_id)
        owner = root / "harness.json"
        entry = skill.get("entrypoint", "")
        definition = skill.get("definition", "")
        if not isinstance(entry, str) or not isinstance(definition, str) or not entry or not definition:
            problem(errors, "harness.json", f"rutas de skill incompletas: {skill_id}")
            continue
        entry_path, error = local_target(root, owner, entry)
        if error or entry_path is None or not entry_path.is_file():
            problem(errors, "harness.json", f"entrypoint inválido: {skill_id}")
            continue
        declared.add(entry_path.relative_to(root).as_posix())
        definition_path, error = local_target(root, owner, definition)
        if error or definition_path is None or not definition_path.is_file():
            problem(errors, "harness.json", f"definición inválida: {skill_id}")
            continue
        try:
            text = entry_path.read_text(encoding="utf-8")
            fields = frontmatter(text)
            if fields.get("name") != skill_id:
                raise ValueError("name distinto del id")
            if not fields.get("description") or len(fields["description"]) > 1024:
                raise ValueError("description vacía o demasiado larga")
            resolved_links = [local_target(root, entry_path, m.group(1))[0] for m in LINK.finditer(text)]
            if definition_path not in resolved_links:
                raise ValueError("el envoltorio no enlaza su definición canónica")
        except (OSError, ValueError) as exc:
            problem(errors, entry, str(exc))
    found = {p.relative_to(root).as_posix() for p in files
             if p.name == "SKILL.md" and ".agents" in p.parts}
    if found != declared:
        problem(errors, "harness.json", "el catálogo y las skills existentes no coinciden")

    cases_count = 0
    evaluation_path = root / "evals" / "casos.json"
    if evaluation_path.exists():
        try:
            evaluation = json.loads(evaluation_path.read_text(encoding="utf-8"))
            cases = evaluation["cases"]
            if not isinstance(cases, list):
                raise ValueError("cases debe ser una lista")
            case_ids: set[str] = set()
            for case in cases:
                if not isinstance(case, dict):
                    raise ValueError("caso inválido")
                case_id = case.get("id")
                if not isinstance(case_id, str) or not case_id or case_id in case_ids:
                    raise ValueError("id de evaluación ausente o duplicado")
                case_ids.add(case_id)
                if not case.get("prompt") or not case.get("must_observe"):
                    raise ValueError("caso sin pedido o criterios observables")
                roles = case.get("expected_roles", [])
                if not isinstance(roles, list) or any(role not in seen for role in roles):
                    raise ValueError("caso refiere a roles no declarados")
            cases_count = len(cases)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            problem(errors, "evals/casos.json", f"evaluaciones no válidas: {exc}")
    return {"ok": not errors, "files": len(files), "skills": len(seen),
            "evaluation_cases": cases_count, "errors": errors,
            "limits": "Validación estructural offline; no prueba eficacia, activación en UI ni conectividad."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate_repository(args.root)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        state = "APROBADO" if result["ok"] else "RECHAZADO"
        print(f"{state}: {result['files']} archivos, {result['skills']} skills, "
              f"{result['evaluation_cases']} escenarios.")
        for error in result["errors"]:
            print(f"- {error}")
        print(result["limits"])
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
