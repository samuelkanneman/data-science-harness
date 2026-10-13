# Uso y adopción

## Abrir este checkout

Leer [AGENTS.md](../AGENTS.md) y el [índice](indice.md). Codex descubre skills de repositorio en .agents/skills; su activación en la interfaz debe comprobarse en una nueva sesión. Se puede pedir una skill por su nombre, por ejemplo $juez, o leer su SKILL.md explícitamente.

La estructura de skills se basa en [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills). Esta preparación valida archivos y referencias; no certifica el selector ni una corrida real.

CLAUDE.md apunta a AGENTS.md para las herramientas que reconocen esa sintaxis. Para otras herramientas, cargar las instrucciones y el rol necesarios por su mecanismo documentado. No se generaron agentes nativos ni permisos para todos los asistentes.

## Aplicar la metodología en otro proyecto

1. Leer el AGENTS, el catálogo de pipelines y las reglas de ese proyecto.
2. Elegir las prácticas necesarias y el perfil de dominio.
3. Completar el [contrato de análisis](../templates/ANALISIS.md) cuando la tarea lo requiera.
4. Mantener referencias que funcionen desde el proyecto de destino. Si se copian skills, deben viajar también sus referencias; copiar solamente los envoltorios rompe el paquete.
5. Validar una tarea offline y después, con autorización, el flujo operacional correspondiente.

Este checkout no se activa automáticamente en repositorios hermanos ni sustituye las skills personales existentes. La instalación en perfiles de usuario, los adaptadores por herramienta y los hooks están en la [hoja de ruta](hoja-de-ruta.md).

## Extender el paquete

Editar la definición canónica en docs/roles o docs/procedimientos. Ajustar el envoltorio y harness.json si cambia nombre, descripción o referencia. Agregar casos de evaluación cuando el cambio afecte decisiones.

Los proyectos declaran sus propias rutas, conexiones, fuentes, marcas y umbrales. El perfil de riesgo no impone sus convenciones a otros dominios.
