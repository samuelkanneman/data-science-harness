"""Casos adversos del verificador; no ejecutan agentes ni bases de datos."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validar_repo.py"
SPEC = importlib.util.spec_from_file_location("validar_repo", MODULE_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("AGENTS.md", "# Instrucciones\n")
        self.write("README.md", "[Rol](docs/demo.md)\n")
        self.write(".gitignore", "data/\n.env\n")
        self.write("docs/demo.md", "# Definición\n")
        self.write(".agents/skills/demo/SKILL.md",
                   '---\nname: demo\ndescription: "Verificar un caso."\n---\n'
                   '[Definición](../../../docs/demo.md)\n')
        self.manifest = {"schema_version": 1, "name": "data-science-harness",
                         "version": "0.1.0", "skills": [
                             {"id": "demo", "entrypoint": ".agents/skills/demo/SKILL.md",
                              "definition": "docs/demo.md"}]}
        self.save_manifest()

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def save_manifest(self):
        self.write("harness.json", json.dumps(self.manifest))

    def result(self):
        return VALIDATOR.validate_repository(self.root)

    def test_valid_portable_package(self):
        result = self.result()
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["skills"], 1)

    def test_missing_reference_is_rejected(self):
        self.write("README.md", "[Ausente](docs/no-existe.md)\n")
        self.assertFalse(self.result()["ok"])

    def test_reference_cannot_escape_checkout(self):
        self.write("README.md", "[Externo](../externo.md)\n")
        self.assertTrue(any("sale del repositorio" in e for e in self.result()["errors"]))

    def test_absolute_windows_path_is_rejected(self):
        drive_path = "C" + ":/" + "local/archivo.md"
        self.write("README.md", f"[Ruta]({drive_path})\n")
        self.assertFalse(self.result()["ok"])

    def test_relative_path_with_spaces_and_anchor(self):
        self.write("docs/con espacios.md", "# Sección\n")
        self.write("README.md", "[Referencia](docs/con%20espacios.md#seccion)\n")
        self.assertTrue(self.result()["ok"], self.result()["errors"])

    def test_https_reference_is_not_a_drive_path(self):
        self.write("README.md", "[Fuente](https://example.org/documento)\n")
        self.assertTrue(self.result()["ok"], self.result()["errors"])

    def test_unc_reference_is_rejected(self):
        unc_path = chr(92) * 2 + "server" + chr(92) + "share"
        self.write("README.md", unc_path)
        self.assertFalse(self.result()["ok"])

    def test_private_environment_file_is_rejected(self):
        self.write(".env", "VALUE=local\n")
        self.assertTrue(any("privada" in e for e in self.result()["errors"]))

    def test_dataset_is_rejected(self):
        self.write("data/real.csv", "columna\nvalor\n")
        self.assertFalse(self.result()["ok"])

    def test_secret_marker_is_rejected(self):
        token = "ghp_" + "A" * 40
        self.write("docs/exposicion.md", token)
        self.assertTrue(any("credencial" in e for e in self.result()["errors"]))

    def test_skill_must_reference_declared_definition(self):
        self.write("docs/otro.md", "# Otro\n")
        self.write(".agents/skills/demo/SKILL.md",
                   '---\nname: demo\ndescription: "Verificar un caso."\n---\n'
                   '[Otro](../../../docs/otro.md)\n')
        self.assertTrue(any("canónica" in e for e in self.result()["errors"]))

    def test_duplicate_catalog_entries_are_rejected(self):
        self.manifest["skills"].append(dict(self.manifest["skills"][0]))
        self.save_manifest()
        self.assertTrue(any("duplicada" in e for e in self.result()["errors"]))

    def test_undeclared_skill_is_rejected(self):
        self.write(".agents/skills/extra/SKILL.md", "---\nname: extra\n---\n")
        self.assertFalse(self.result()["ok"])

    def test_unknown_role_in_evaluation_is_rejected(self):
        self.write("evals/casos.json", json.dumps({"cases": [
            {"id": "caso", "prompt": "Revisar", "must_observe": ["Evidencia"],
             "expected_roles": ["ausente"]}]}))
        self.assertTrue(any("roles no declarados" in e for e in self.result()["errors"]))


if __name__ == "__main__":
    unittest.main()
