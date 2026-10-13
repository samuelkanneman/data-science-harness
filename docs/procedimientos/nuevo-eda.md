# nuevo-eda — exploración de un dataset

**Responsable:** [lupa](../roles/lupa.md). Presentación: [vitrina](../roles/vitrina.md).

**Entradas:** dataset ya extraído, pregunta, unidad de análisis, clave, población, período, target o métrica y destinatario. Aplicar [método](../metodo.md) y [convenciones](../convenciones.md).

## Procedimiento

1. Buscar el proyecto al que pertenece el dataset y leer `AGENTS.md`. Reutilizar una estructura existente. Si hace falta un proyecto nuevo, usar brujula dentro del alcance autorizado; una revisión del dataset no autoriza crearlo.
2. Leer con esquema, separador, decimal y encoding explícitos. Para el perfil es-AR: `;`, `,`, `utf-8-sig` y fallback `cp1252`; no detectar silenciosamente un formato distinto. Contar NaN introducidos por coerción.
3. Confirmar clave, target, segmentos y período. Resolver ambigüedad de negocio antes del análisis dependiente; usar [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md) si corresponde.
4. Construir el notebook reutilizando patrones locales: perfil de filas y tipos, nulos, duplicados, fechas y volumen; distribuciones numéricas y categóricas; target o métrica; cruces pertinentes y correlaciones cuando aporten.
5. En tasas, mostrar sumas de numeradores y denominadores, n y perímetro. Para riesgo, separar refinanciaciones, controlar selección y comparar cohortes con la misma madurez.
6. Redactar entre tres y siete hallazgos con cifra y n. Separar evidencia, hipótesis y recomendación; declarar límites y fuentes.
7. Exportar el HTML después de ejecutar y guardar, mediante el mecanismo documentado del destino. Usar gráficos interactivos cuando ayuden y Plotly embebido en entregables. Aplicar formato y paleta del destinatario.
8. Verificar contenido, período, al menos tres cifras contra la fuente, lectura sin red y `mtime` nuevo. Si no se autorizó la ejecución, entregar la implementación y dejar esos controles pendientes.
9. Documentar entradas, comando y salidas en el proyecto y aplicar [cierre](cierre.md).

## Entrega

Notebook, HTML si fue generado y verificado, tablas y hallazgos. Los datos del negocio no se agregan al repositorio público; para ejemplos, usar datos sintéticos.
