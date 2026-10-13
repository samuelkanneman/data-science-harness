# nuevo-dashboard — dashboard reproducible

**Responsable:** [vitrina](../roles/vitrina.md). Métricas: [juez](../roles/juez.md).

**Entradas:** resultados o datos autorizados, destinatario, pregunta, filtros, período y definiciones. Aplicar [método](../metodo.md) y [convenciones](../convenciones.md).

## Procedimiento

1. Localizar proyecto, guía de estilos y constructor vigente en el catálogo del destino. Leer `AGENTS.md` y respetar su arquitectura, contratos de datos y comportamientos requeridos.
2. Leer las fuentes con formato declarado. Identificar clave, target o métrica, score si existe, fecha y segmentos. Resolver faltantes que cambien el resultado.
3. Reutilizar una base existente. Si se autoriza un proyecto nuevo, crear solo estructura, configuración, entradas y salidas necesarias mediante brujula; documentar el comando real del destino.
4. Obtener métricas desde implementaciones canónicas. En riesgo, usar [definiciones](../perfiles/riesgo-crediticio/DEFINICIONES.md): KS por deciles, AUC con orientación explícita y PSI con referencia fija. Declarar manejo de empates y deciles no formados; no crear variantes silenciosas.
5. Construir resumen, indicadores, tablas y gráficos con filtros que conserven población y denominadores coherentes. Mostrar período, perímetro, target o métrica, fuente y corte.
6. Generar HTML autocontenido con Plotly embebido una sola vez. Aplicar accesibilidad, formato regional y paleta del destinatario; las dependencias del entregable deben permitir lectura sin red.
7. Verificar apertura offline, filtros relevantes, al menos tres cifras contra la fuente, período y `mtime` nuevo. Si no se hizo una prueba visual, declararlo.
8. Solicitar centinela para una entrega de gestión, documentar el uso y aplicar [cierre](cierre.md).

## Límites

No extraer datos ni recalcular definiciones como efecto lateral del diseño. Una publicación exige autorización para esa acción. Nunca incorporar datos personales o secretos a un dashboard público.
