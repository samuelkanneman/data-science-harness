# veta — extracción de datos

**Propósito:** preparar un dataset crudo reproducible y validado, con grano, clave, fechas y controles explícitos.

**Cuándo usar:** escribir o ejecutar consultas autorizadas, expandir campos estructurados o integrar fuentes externas según su disponibilidad temporal. El EDA corresponde a [lupa](lupa.md), las métricas a [juez](juez.md) y las corridas existentes a [maquinista](maquinista.md).

## Contexto mínimo

Leer `AGENTS.md`, diccionario de datos, catálogo de conexiones y gotchas del destino. Aplicar [método](../metodo.md), [convenciones](../convenciones.md) y, en riesgo crediticio, [definiciones](../perfiles/riesgo-crediticio/DEFINICIONES.md).

## Límites

- Preparar una consulta no autoriza su ejecución. Respetar pedidos de revisión o preparación sin corrida.
- En el DW, solo `SELECT`. No probar escrituras, ni siquiera con rollback. Una configuración de sesión de lectura permitida por el proyecto se ejecuta por separado.
- Usar conexiones restringidas y secretos provistos por el entorno; no escribir credenciales ni exponerlas en logs.
- No extraer datos personales a entregables públicos. Los archivos del negocio quedan en almacenamiento autorizado, fuera de este harness.

## Procedimiento

1. Declarar población, ventana, unidad de análisis, clave, fecha ancla y fecha de corte. Resolver ambigüedades antes de una extracción que dependa de ellas.
2. Reutilizar consultas y utilidades vigentes. Para una consulta nueva autorizada, probar una muestra acotada con el mecanismo del motor y medir tiempo; después ejecutar el alcance completo con timeout.
3. Revisar las fechas: para campos datetime, usar límite superior exclusivo que incluya el último día solicitado. Aplicar el dialecto y las restricciones documentadas del motor.
4. Guardar la consulta y los parámetros reproducibles en el proyecto. Cachear el crudo según sus convenciones y registrar fuente, período, corte y esquema.
5. Validar filas por período, nulos en claves, rango de fechas, totales y unicidad. Hacer un assert de la clave declarada antes de guardar; no asumir que un número de operación aislado es único.
6. Integrar fuentes con cardinalidad declarada. En cruces temporales, elegir el último registro disponible antes de la decisión; informar tolerancia, rezago y faltantes. El conocimiento futuro no puede entrar como variable histórica.
7. Entregar el dataset y sus controles al siguiente rol.

## Notas del perfil de riesgo

Para Informix, aplicar los patrones verificados del destino: un statement por ejecución, fechas `DATETIME(...) YEAR TO DAY`, aislamiento de lectura configurado por separado y casts explícitos de montos y conteos. Procesar listas `IN` en lotes de hasta 900; sin joins entre bases distintas. Normalizar CHAR y nombres de columnas.

Los datos regulatorios o de buró se anclan a la fecha de decisión y a su demora real de publicación; aplicar el rezago definido en el perfil y en el proyecto. Cuando la fuente exige dos meses de demora, el período de referencia es M−2, no el mes de la decisión.

## Entrega

Grano, clave, filas por período, exclusiones, controles, duración y ubicación del crudo. En errores de conexión, informar etapa, operación y códigos depurados; retirar SQL sensible, identificadores y secretos del diagnóstico compartido.
