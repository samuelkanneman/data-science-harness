# cierre — continuidad documental

**Objetivo:** permitir que otra sesión retome el trabajo sin reconstruir decisiones ni repetir errores. Aplicar el [método](../metodo.md) y las [convenciones](../convenciones.md) del destino.

## Procedimiento

1. Reunir resultado, decisiones, controles ejecutados, archivos, limitaciones y pendientes. Distinguir implementación, verificación offline y validación operacional.
2. Para trabajo que produjo cambios, registrar una entrada fechada en la bitácora del proyecto: qué se hizo, por qué, evidencia y próximo paso. Una consulta de solo lectura se cierra con la respuesta; no genera escrituras por este procedimiento.
3. Mantener `AGENTS.md` con lo vigente, hasta 200 líneas. La historia y los experimentos descartados van a la bitácora. Si se creó un proyecto autorizado, usar las plantillas y registrar su ubicación en el catálogo del destino.
4. Registrar gotchas reutilizables en el conocimiento común según su esquema de IDs. Incluir síntoma, causa, solución, alcance, fecha y fuente; conservar los IDs existentes. Los detalles exclusivos del proyecto quedan allí.
5. Actualizar definiciones, diccionarios o glosario solo con hechos verificados y dentro del alcance. Fechar correcciones y explicar contradicciones; no importar conversaciones ni memorias en bloque.
6. Registrar bugs fuera del encargo y comprobaciones pendientes en el backlog apropiado. Indicar responsable o evidencia necesaria para continuar; no hacer arreglos laterales.
7. Si el cambio corresponde a un proyecto conectado a un catálogo, actualizar su estado sin modificar otros proyectos.
8. Informar resultado, archivos, evidencia y pendientes, incluidos cambios Git sin publicar cuando corresponda.

## Límites

- La memoria privada de una herramienta solo se actualiza ante pedido directo del usuario, mediante el mecanismo permitido por esa herramienta. El conocimiento común durable se conserva en archivos del proyecto.
- No actualizar configuraciones o reglas del workspace de origen desde una decisión del paquete portable.
- No hacer commits, push, publicación ni instalación automáticos. Conservar autorizaciones explícitas ya concedidas para ese alcance.
- No documentar datos personales, secretos, SQL sensible ni fuentes corporativas en el repositorio público.

## Evidencia mínima de cierre

Estado real del trabajo, comprobaciones observadas, pendientes y siguiente acción reproducible. Una comprobación no ejecutada sigue pendiente aunque el código esté terminado.
