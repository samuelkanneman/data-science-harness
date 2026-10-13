# lupa — exploración y segmentación

**Propósito:** entender los datos y entregar hallazgos cuantificados con población, tamaño de muestra y límites de interpretación.

**Cuándo usar:** EDA, perfilado, segmentación y análisis observado/esperado. Parte de datos ya extraídos; no consulta el DW ni construye el informe final, tareas de [veta](veta.md) y [vitrina](vitrina.md).

## Contexto mínimo

Leer `AGENTS.md`, el contrato del análisis y el glosario del destino. Aplicar [método](../metodo.md), [convenciones](../convenciones.md) y las [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md) cuando correspondan.

## Procedimiento

1. Perfilar filas, columnas, tipos, período, grano, clave, duplicados, nulos, target y volumen por período. Investigar quiebres de carga antes de interpretarlos como negocio.
2. Declarar target, perímetro, ventana y corte. Si no hay target, describir la métrica o pregunta exploratoria sin inventarlo.
3. Revisar distribuciones y relación con las variables del encargo. Mostrar n y denominador en cada tasa; distinguir operaciones, personas y montos.
4. Contrastar los cruces con controles pertinentes, como nivel de riesgo y cohorte. Para grupos con distinto mix, usar una comparación estandarizada y declarar la referencia.
5. Separar hecho observado, hipótesis y recomendación. La asociación por segmento no demuestra causalidad ni riesgo puro.
6. Entregar entre tres y siete hallazgos con cifra, n, período, perímetro y confianza, más tablas y figuras reproducibles para vitrina.

## Reglas

- Tasas agregadas mediante suma de numeradores dividida por suma de denominadores; nunca promediar índices. Declarar qué sucede con denominadores cero.
- Mostrar el soporte muestral. En el perfil de riesgo, celdas con menos de 30 operaciones se agrupan cuando tenga sentido o se marcan como inestables; ese umbral no convierte las demás celdas en concluyentes.
- Leer CSV con separador, decimal y encoding declarados. Contar los NaN introducidos por toda coerción numérica; no convertir un target desconocido en un caso favorable.
- En riesgo, refinanciaciones separadas o perímetro total explícito. Comparar cohortes con la misma madurez y ventana de observación.
- Revisar selección, aprobación y restricción de rango antes de atribuir diferencias a un modelo o a un grupo.
- Usar el score continuo cuando se evalúe ordenamiento; no sustituirlo por una etiqueta comercial sin justificación.
- En el perfil de riesgo, atraso se refiere a conteos y mora al índice monetario. No mezclar denominadores.

## Entrega

Tabla de hallazgos y rutas de las fuentes, tablas y figuras. Cada conclusión indica qué controles resistió y cuáles no se pudieron verificar.
