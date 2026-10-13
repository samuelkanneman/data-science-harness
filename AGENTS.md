# AGENTS.md — data-science-harness

**Objetivo:** conservar y evolucionar una metodología portable para trabajar con agentes en ciencia de datos, con evidencia de ejecución y validez del análisis.
**Estado:** ACTIVO, publicado en GitHub · 2026-10-13 · responsable: brujula.
**Repositorio:** https://github.com/samuelkanneman/data-science-harness (público).

## Inicio

1. Leer este archivo y `README.md`.
2. Si este checkout está dentro de un workspace con reglas superiores, leerlas y respetarlas. En el workspace original de Samuel corresponden las instrucciones de la raíz y su WIKI/CODEX.md; la exportación no las reemplaza.
3. Consultar `docs/indice.md` y cargar solo las referencias necesarias para la tarea.
4. Las definiciones canónicas están en `docs/roles/` y `docs/procedimientos/`. Las skills son envoltorios que apuntan a ellas.

## Alcance y permisos

- Responder y documentar en español.
- Conservar el alcance y la autorización del usuario. Una consulta o revisión es de solo lectura.
- Reutilizar proyectos, runners y métricas existentes; comprobar el catálogo del proyecto de destino antes de crear un flujo.
- Ejecutar consultas de datos solo con autorización para la extracción correspondiente y mediante conexiones restringidas. En el perfil de riesgo crediticio, las consultas al DW son solo SELECT; no probar escrituras ni siquiera con rollback.
- Solicitar información de negocio que cambie el resultado; conservar las respuestas entre turnos.
- No realizar commits, pushes, publicaciones ni instalaciones sin un pedido que autorice esa acción. Preparar archivos no implica publicar.
- No guardar credenciales, datos personales, fuentes corporativas ni transcripciones en este repositorio. Los ejemplos deben ser sintéticos.
- Los roles expresan instrucciones. No atribuirles restricciones técnicas que no estén configuradas y comprobadas en la herramienta utilizada.

## Método

- Consulta: respuesta con fuentes y límites; sin escrituras ni nuevos proyectos.
- Corrida recurrente: procedimiento existente, parámetros permitidos y controles de salidas.
- Cambio acotado: alcance, tareas y evidencia en un único registro.
- Trabajo complejo: contrato del análisis, plan, decisiones y revisión proporcional al riesgo.
- Declarar unidad de análisis, clave, población, target o métrica, ventana y fecha de corte cuando correspondan.
- Distinguir implementación, validación offline y validación operacional. Una comprobación no ejecutada queda pendiente.
- Para modelos: separar ajuste, selección y evaluación; controlar leakage, madurez del target y sesgo de selección.

## Colaboración

- Delegar cuando las reglas del proyecto o la tarea lo indiquen y la herramienta lo permita. No activar todos los roles por defecto.
- En paralelo, solo trabajos independientes; dos agentes no escriben el mismo archivo. Dentro de un repositorio Git, los editores concurrentes usan worktrees separados.
- Las extracciones pesadas contra una misma base se ejecutan en secuencia.
- El auditor trabaja en solo lectura y presenta evidencia para cada hallazgo.

## Verificación y cierre

- Intérprete: Python 3.10 o posterior; los scripts del harness usan biblioteca estándar. En el workspace original se usa el intérprete indicado por sus reglas.
- Ejecutar `python scripts/validar_repo.py` después de modificar el paquete.
- Ejecutar `python -m unittest discover -s tests` después de modificar sus scripts.
- Registrar decisiones e historia en `BITACORA.md`; mantener este archivo con lo vigente, hasta 200 líneas.
- No modificar las instrucciones del workspace original por una decisión tomada únicamente para este paquete portable.
- Las mejoras propuestas y los límites de validación se documentan en `docs/hoja-de-ruta.md`.
