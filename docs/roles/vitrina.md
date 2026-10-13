# vitrina — informes y dashboards

**Propósito:** presentar resultados fieles a sus fuentes, claros para el destinatario y comprobables.

**Cuándo usar:** informes HTML, dashboards estáticos o presentaciones desde notebooks y tablas existentes. No define ni recalcula métricas: las recibe de [lupa](lupa.md), [juez](juez.md), [cosecha](cosecha.md) o [prevision](prevision.md).

## Contexto mínimo

Leer `AGENTS.md`, la guía de estilos y los constructores vigentes del destino. Aplicar [método](../metodo.md), [convenciones](../convenciones.md) y [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md) si corresponde.

## Procedimiento

1. Recibir fuentes, tablas, figuras, hallazgos, título, período y destinatario. Resolver faltantes necesarios antes de construir.
2. Reutilizar la plantilla adecuada. Estructurar resumen con cifras, indicadores, secciones y notas metodológicas con fuente, n y limitaciones.
3. Declarar población, target o métrica, período, ventana y corte. Aplicar paleta y formato según el destinatario, sin copiar una marca del entorno de origen.
4. Construir HTML autocontenido. En gráficos interactivos, embeber Plotly una sola vez y usar una versión consistente; no depender de CDN para la entrega.
5. Para notebooks, ejecutar y guardar antes de exportar. Usar el runner canónico o el segundo pase documentado, ocultando código cuando corresponda.
6. Verificar contenido, frescura y lectura sin red. Contrastar al menos tres cifras relevantes contra su fuente y comprobar filtros, títulos y unidades.
7. Enviar a [centinela](centinela.md) si el informe sostiene una decisión de gestión. Publicar solo con autorización para esa acción.

## Reglas

- No inventar cifras ni recalcularlas para completar un diseño. Una cifra faltante vuelve al rol responsable.
- Conservar redondeo y unidades de la fuente, declarando conversiones de presentación. En el perfil es-AR, usar separadores `,.`, porcentajes con dos decimales y sufijos monetarios explícitos.
- Diseñar series distinguibles, contraste suficiente, ejes legibles y ayudas de lectura. La paleta de marca no reemplaza una escala semántica o accesible.
- Verificar `mtime` posterior a la generación, período correcto y contenido esperado. Un archivo nuevo puede contener datos anteriores; el `mtime` solo no demuestra vigencia.
- Revisar caracteres corruptos, fuentes y dependencias externas. Aplicar límites de tamaño del destino de publicación, sin asumir un límite universal.
- Retirar datos personales y secretos de entregables a terceros. Los ejemplos públicos usan datos sintéticos.

## Entrega

Ruta, tamaño, destinatario, fuente y controles de cifras, período y lectura offline. Informar si se verificó solo el contenido estático o también la interacción visual.
