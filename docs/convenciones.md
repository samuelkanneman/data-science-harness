# Convenciones portables

Actualizado: 2026-10-13. Son valores iniciales de esta metodología; el contrato del proyecto puede declarar excepciones.

## Datos y archivos

- En el perfil original: CSV con separador punto y coma, decimal coma y lectura UTF-8 con BOM tolerado; si falla la decodificación, probar CP1252.
- Declarar formato en el contrato del dataset. Conservar formatos existentes mientras sus lectores dependan de ellos; una migración es una tarea explícita.
- Después de conversión numérica con coerción, contar los valores faltantes que aparecieron y decidir su tratamiento.
- Declarar grano y clave; comprobar unicidad antes de guardar. Informar filas, duplicados, exclusiones y pérdidas en joins.
- Separar datos crudos, procesados y entregables dentro del proyecto de destino. Este repo mantiene ejemplos sintéticos en JSON.

## Entorno y parámetros

Declarar intérprete, versiones y dependencias. Invocar el intérprete explícito del proyecto; un comando python sin resolver su entorno no acredita reproducibilidad. Las dependencias de un pipeline se fijan o bloquean según el proyecto; este paquete de instrucciones usa biblioteca estándar.

Usar una sola fuente de parámetros. Fechas humanas inclusivas; derivar el día siguiente como límite exclusivo cuando la fuente almacena fecha y hora. Declarar zona horaria. Buscar y elegir directorios existentes cuando sus nombres son convenciones humanas.

## Bases y herramientas

Usar las conexiones autorizadas del proyecto. Mantener secretos en DSN o entorno local, fuera del repositorio. Para el perfil de riesgo crediticio, las consultas al DW son SELECT; una operación de configuración de sesión permitida se ejecuta por separado y no concede permiso de escritura.

No probar restricciones intentando INSERT, CREATE u otra escritura con rollback. Las comprobaciones de permisos se basan en configuración, permisos consultables y cuentas restringidas. La conectividad real sigue siendo una validación operacional autorizada.

## Notebooks y salidas

Usar runners existentes. Identificar entradas, orden, celdas-freno y parámetros editables antes de ejecutar.

Registrar inicio, fin, comando, estado y salidas esperadas. Para artefactos que deben regenerarse, comprobar mtime posterior al inicio y contenido coherente. Un pipeline idempotente puede conservar entradas o CSV sin cambios si el contrato lo permite y hay evidencia.

Cuando la exportación dentro de un notebook puede capturar su estado anterior, usar el runner correcto o un segundo pase de exportación. Verificar hashes de copias cuando una entrega depende de archivos idénticos.

## Informes

Declarar fuente, corte, población, métrica, limitaciones y destinatario. Elegir identidad visual según el destinatario, mediante configuración del proyecto. Entregables HTML autocontenidos con Plotly embebido cuando se usa esa librería. En el perfil es-AR, decimal coma y miles punto.

## Documentación y Git

AGENTS hasta 200 líneas con instrucciones vigentes; BITACORA conserva decisiones e historia. Cargar referencias por necesidad. Las rutas del paquete son relativas al checkout; las rutas operativas de un proyecto se resuelven y documentan en ese entorno.

Una definición por rol o procedimiento. Los envoltorios apuntan a ella. Los cambios de este paquete no actualizan automáticamente instalaciones ni la WIKI que le dio origen.

Preservar cambios locales. Commits, pushes y publicaciones se realizan cuando el usuario los pide. No activar sincronización automática ni hooks durante la preparación del paquete.
