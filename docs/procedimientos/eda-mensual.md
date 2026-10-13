# eda-mensual — EDA periódico existente

**Responsable:** [maquinista](../roles/maquinista.md). Análisis adicional: [lupa](../roles/lupa.md).

**Alcance:** usar el pipeline formalizado del destino, con sus parámetros y salidas. Si no existe uno adecuado, resolver el alcance con brujula y [nuevo-eda](nuevo-eda.md); no inventar una corrida mensual.

## Preparación

Leer `AGENTS.md`, catálogo, procedimiento local y [convenciones](../convenciones.md). Confirmar fecha de inicio y fin, corte, fuentes listas y autorización de ejecución. El comando e intérprete salen del proyecto.

## Procedimiento

1. Anotar inicio y verificar insumos. En campos datetime, comprobar que el filtro incluya el último día solicitado; un corte parcial se declara.
2. Leer qué parámetro controla la corrida. Si el runner deriva fechas y genera configuración, modificar únicamente el parámetro admitido; no editar a mano archivos generados.
3. Mostrar diff y ejecutar el runner vigente. Respetar orden de extracción, preparación, EDA y armado del informe; conservar celdas-freno y controles de datos.
4. Verificar todas las salidas declaradas en el catálogo: tablas, HTML exploratorios e informe. Comprobar existencia, `mtime` nuevo, período, contenido y ausencia de marcas de desactualización.
5. Confirmar que el notebook se guardó antes de exportar. Aplicar el segundo pase vigente si se necesita para obtener un HTML fresco.
6. Revisar conteos, nulos, tasas y volúmenes contra una referencia equivalente. Para riesgo crediticio, usar [definiciones](../perfiles/riesgo-crediticio/DEFINICIONES.md), mostrar n y separar refinanciaciones según el perímetro.
7. Entregar evidencia operacional y aplicar [cierre](cierre.md).

## Límites

No modificar análisis, umbrales, estilos ni destinos de salida durante una corrida. Los errores se diagnostican con evidencia depurada. Aplicar permisos efectivos de la herramienta; una dificultad de conexión no autoriza cambiar restricciones.
