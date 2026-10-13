# html-desde-eda — informe desde resultados existentes

**Responsable:** [vitrina](../roles/vitrina.md).

**Entradas:** notebook ejecutado o tablas de resultados, fuentes, pregunta, destinatario y período. Reutilizar guía de estilos y constructor del destino; aplicar [método](../metodo.md) y [convenciones](../convenciones.md).

## Procedimiento

1. Leer el EDA y verificar su período, población, target o métrica y fecha de corte. Confirmar destinatario y autorización de generación; no confundir un pedido de revisión con uno de modificación.
2. Si es notebook, preservar su fuente y celdas de análisis. Preparar la presentación mediante una copia o mecanismo local autorizado: ocultar celdas auxiliares y código, agregar encabezado y mejorar gráficos cuando ayude a la lectura.
3. Si son tablas, leerlas con formato explícito y construir la presentación sin redefinir cálculos. Un número faltante se solicita al responsable del análisis.
4. Estructurar resumen con cifras, indicadores, secciones y notas metodológicas con fuente, n, exclusiones y limitaciones. En riesgo, aplicar [definiciones](../perfiles/riesgo-crediticio/DEFINICIONES.md) y declarar refinanciaciones.
5. Aplicar paleta y formato regional del destinatario. Embeber Plotly una sola vez cuando haya gráficos interactivos; conservar figuras estáticas cuando sean adecuadas.
6. Para exportar desde notebook, guardar las salidas ejecutadas antes de leerlo de disco. Usar el runner o segundo pase documentado y un nombre de archivo descriptivo.
7. Verificar `mtime`, título y período, al menos tres cifras contra la fuente y lectura sin red. Revisar caracteres corruptos, fuentes y dependencias.
8. Para publicación, comprobar datos personales, secretos y límites efectivos del destino. Solicitar centinela si sostiene una decisión de gestión; publicar solo dentro de la autorización concedida.
9. Entregar archivo y evidencia, y aplicar [cierre](cierre.md).

## Límites

Este procedimiento mejora la presentación; no autoriza una nueva extracción, una corrida del EDA ni un cambio metodológico. Si la fuente está desactualizada, informar qué falta actualizar y conservar la generación dependiente pendiente.
