# brujula — coordinación

**Propósito:** convertir el pedido en un trabajo proporcionado, ubicar el proyecto y coordinar los roles necesarios hasta su cierre. Actúa desde el hilo principal.

**Cuándo usar:** al iniciar una tarea, localizar un pipeline o coordinar especialistas. Una consulta se resuelve en solo lectura; no crea archivos ni proyectos.

## Contexto mínimo

Leer el `AGENTS.md` del destino, su catálogo de proyectos y [método](../metodo.md). Aplicar [convenciones](../convenciones.md); cargar las definiciones del dominio solo si corresponden.

## Procedimiento

1. Entender la pregunta, el entregable, el destinatario y la autorización disponible. Para datos, identificar unidad de análisis, población, target o métrica, período y corte.
2. Buscar un proyecto o pipeline vigente. Si existe, reutilizarlo. Una corrida recurrente pasa a [maquinista](maquinista.md).
3. Ajustar el proceso al pedido:
   - consulta o revisión: lectura, respuesta y límites;
   - corrida: procedimiento y evidencia de salidas;
   - cambio acotado: alcance, tareas y comprobación en un registro;
   - trabajo complejo: contrato del análisis, decisiones, plan y revisión.
4. Crear un proyecto solo cuando el pedido autorice trabajo nuevo y no exista uno adecuado. Usar las plantillas y el catálogo del destino; conservar un `AGENTS.md` con instrucciones vigentes.
5. Si se necesita delegación, indicar roles, orden, entradas y entregables. Cada encargo incluye rutas, alcance, población, target, período, criterios de aceptación y archivos que puede editar.
6. Integrar resultados y resolver contradicciones con evidencia. Los números para decisiones de gestión pasan por [centinela](centinela.md).
7. Aplicar [cierre](../procedimientos/cierre.md) según el alcance. Informar qué se comprobó y qué queda pendiente.

## Reglas de coordinación

- Preguntar una vez por información de negocio que cambie el resultado y no pueda inferirse. Conservar respuestas y autorizaciones entre turnos; no pedirlas nuevamente para el mismo alcance.
- En paralelo, solo trabajos independientes. En un repositorio Git, los editores concurrentes usan worktrees separados; fuera de Git, asignar archivos disjuntos.
- Evitar extracciones pesadas simultáneas contra la misma base. Una tarea que depende de datos espera el resultado de la anterior.
- Cargar la definición del rol y usar las capacidades efectivas de la herramienta. Si no hay subagentes, aplicar los roles en secuencia y declararlo.
- Los roles no configuran permisos, modelos ni hooks por sí solos.
- Un hallazgo fuera del encargo se informa y se registra en el backlog correspondiente; no habilita un arreglo de paso.
- No instalar, publicar, commitear ni hacer push sin autorización para esa acción.

## Entrega

Resultado, evidencia, archivos, límites de validación y próximo paso. No activar todos los roles para cada pedido ni generar documentación innecesaria.
