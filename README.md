# data-science-harness

Metodología personal de Samuel Kanneman para trabajar con agentes de IA en ciencia de datos: contexto, roles, procedimientos, validación y trazabilidad.

Esta primera versión portable conserva prácticas desarrolladas en un workspace de riesgo crediticio y las organiza para reutilizarlas en otros proyectos. Un análisis puede ejecutarse sin errores y responder mal la pregunta; por eso se revisan tanto la ejecución como sus definiciones, datos y conclusiones.

## Qué contiene

- Diez roles especializados y siete procedimientos, con una sola definición canónica.
- Diecisiete skills de repositorio que apuntan a esas definiciones.
- Contratos de análisis, tareas, experimentos y evidencia de corridas.
- Una [plantilla de manifiesto](templates/CORRIDA.json) para registrar una ejecución y sus comprobaciones.
- Un perfil opcional de riesgo crediticio con definiciones y errores transferibles.
- Casos offline para evaluar decisiones de los agentes.
- Un verificador de estructura, referencias y señales de contenido que no debe publicarse.

El paquete no modifica la configuración personal de ningún asistente ni ejecuta pipelines al abrirse. Destino: [samuelkanneman/data-science-harness](https://github.com/samuelkanneman/data-science-harness), repositorio público elegido para la primera subida. La licencia de distribución sigue pendiente de elección.

## Empezar

1. Clonar el repositorio cuando esté publicado y abrirlo con el asistente elegido.
2. Leer [AGENTS.md](AGENTS.md) y el [índice](docs/indice.md).
3. Usar el [método](docs/metodo.md) y el perfil correspondiente a la tarea.
4. Para aplicar el harness en otro proyecto, seguir [uso y adopción](docs/uso.md).

Los scripts necesitan Python 3.10 o posterior y usan biblioteca estándar:

```powershell
python scripts/validar_repo.py
python -m unittest discover -s tests
```

En un workspace con intérprete obligatorio, invocarlo mediante su ruta absoluta. La validación local no acredita conectividad a datos, activación de skills en una interfaz ni eficacia de los agentes.

## Organización

```text
AGENTS.md                   reglas de este paquete
.agents/skills/             envoltorios de skills para el repositorio
docs/roles/                 diez definiciones canónicas
docs/procedimientos/        siete procedimientos reutilizables
docs/perfiles/              convenciones específicas de un dominio
templates/                  contratos y registros adaptables
examples/                   ejemplos sintéticos
evals/                      escenarios y criterios observables
scripts/                    comprobaciones offline
tests/                      pruebas de las comprobaciones
harness.json                inventario y trazabilidad de la exportación
```

Las referencias dentro del paquete son relativas al checkout. Las conexiones, rutas operativas, políticas y marcas se declaran en cada proyecto de destino.

## Evolución

El repositorio es independiente de rsc-harness. Las ideas de la comunidad se registran con fuente, motivo, adaptación y evidencia, como explica [el proceso de adopción](docs/adopcion-comunidad.md). Las influencias iniciales están en [referencias](docs/referencias.md).

Consultar [la hoja de ruta](docs/hoja-de-ruta.md), [la bitácora](BITACORA.md) y [la preparación de la primera subida](docs/primera-subida.md).
