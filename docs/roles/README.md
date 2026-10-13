# Catálogo de roles

| Rol | Responsabilidad |
|---|---|
| [brujula](brujula.md) | Clasificar, coordinar y cerrar según el alcance |
| [veta](veta.md) | Extraer y validar datos autorizados |
| [lupa](lupa.md) | EDA, perfiles y segmentación |
| [forja](forja.md) | Construir, entrenar y explicar modelos |
| [juez](juez.md) | Validar discriminación, estabilidad y comparaciones |
| [cosecha](cosecha.md) | Vintage, cohortes y proyecciones |
| [prevision](prevision.md) | Pérdida esperada y conciliación |
| [vitrina](vitrina.md) | Informes y dashboards |
| [maquinista](maquinista.md) | Operar pipelines existentes |
| [centinela](centinela.md) | Auditoría independiente de solo lectura |

Usar solo los roles necesarios. El dominio y las métricas se declaran en el contrato; cosecha y prevision son especialistas del perfil de riesgo.

Recetas: extracción → EDA → presentación → auditoría; construcción de modelos → validación independiente; corrida recurrente → comprobaciones de salidas. Ejecutar en paralelo solo actividades independientes.

Los envoltorios viven en [.agents/skills](../../.agents/skills). Una definición de rol no registra por sí sola un tipo de subagente en cada herramienta.
