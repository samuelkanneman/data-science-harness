# Método de trabajo

Actualizado: 2026-10-13. Esta es la base común; las definiciones de un dominio viven en su perfil y las de una operación en el proyecto que la ejecuta.

## Elegir el recorrido

| Pedido | Trabajo y registro |
|---|---|
| Consulta, investigación o revisión | Leer, verificar y responder. No crear archivos, proyectos ni cierre con escrituras por defecto. |
| Corrida recurrente autorizada | Reutilizar el runner; cambiar solo parámetros permitidos; registrar evidencia y controles. |
| Cambio acotado autorizado | Un [registro de tarea](../templates/TAREA.md) cuando ayude a continuar el trabajo; alcance, criterios y comprobaciones. |
| Análisis o cambio con decisiones dependientes | [Contrato de análisis](../templates/ANALISIS.md), plan, responsables, decisiones y revisión proporcional al impacto. |

El tamaño del código no decide el recorrido. La ambigüedad sobre población, target, comparación, entrega o efectos externos sí puede exigir un contrato más explícito. Conservar el trabajo terminado si una tarea necesita ampliar su planificación.

## Contrato del análisis

Antes de producir un resultado, identificar la pregunta y la decisión que ayudará a tomar. Declarar unidad de análisis, clave, población y exclusiones, período, corte, fuente y disponibilidad temporal.

Cuando hay target, declarar evento, ventana, umbral, madurez y censura. Cuando hay comparación, fijar una población y definición compatibles o explicar las diferencias. En una inferencia causal, declarar diseño, exposición, grupo de comparación y supuestos; una asociación no acredita un efecto.

Preguntar al comienzo solo las dudas que cambian el resultado y no se resuelven con evidencia. Las respuestas y autorizaciones conservan su alcance entre turnos.

## Roles y delegación

Elegir especialistas del [catálogo](roles/README.md). Una skill guía el trabajo; no garantiza un proceso separado ni permisos propios.

Cada encargo informa pregunta, rutas, entradas, salidas, definiciones, período, criterios de aceptación y límites. Delegar solo con soporte y autorización en la herramienta. Si se permiten editores concurrentes dentro de un repo Git, usar worktrees separados. Serializar consultas pesadas contra una misma base.

El revisor independiente recibe el pedido y sus cambios autorizados, los artefactos y la forma de verificar; debe formar su conclusión antes de leer la defensa del autor.

## Evidencia y estados

- Propuesto: alcance o diseño todavía no implementado.
- Implementado: existen los archivos o cambios; la ejecución necesaria puede seguir pendiente.
- Verificado offline: comprobaciones con fixtures o datos sintéticos; no acredita producción.
- Validado operacionalmente: corrida sobre el entorno y perímetro declarados, con salidas verificadas.
- Pendiente o bloqueado: indicar la comprobación que falta y la condición necesaria para continuar.

Una casilla marcada debe enlazar o describir evidencia observada. Un código de salida cero no prueba integridad de claves, corte correcto ni frescura de un informe.

## Entrega y cierre

Aplicar la [auditoría de datos](auditoria-datos.md) según el riesgo del resultado. Registrar hallazgos con ubicación, mecanismo e impacto. Separar defectos comprobados, preguntas y preferencias; comprobar un hallazgo antes de cambiar código.

Cerrar las tareas con cambios mediante [cierre](procedimientos/cierre.md). La publicación, la instalación y Git requieren autorización acorde al pedido; nunca se deducen de terminar un análisis.
