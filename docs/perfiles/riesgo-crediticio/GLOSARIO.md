# Glosario del perfil de riesgo crediticio

Vocabulario portable. Las fórmulas y convenciones acordadas están en [DEFINICIONES.md](DEFINICIONES.md); su adopción se explica en [README.md](README.md). No incluye códigos de clientes ni políticas de aprobación.

## Datos y decisión

| Término | Significado en este perfil |
|---|---|
| Solicitud | Pedido de crédito; puede no terminar en una operación otorgada |
| Operación | Contrato u otorgamiento identificado según su clave de negocio |
| Unidad de análisis | Entidad representada por una fila: solicitud, operación, cliente, cliente-mes u otra unidad declarada |
| Perímetro | Población incluida y exclusiones aplicadas; por ejemplo, total o sin refinanciaciones |
| Refi / refinanciación | Operación que reestructura una obligación según el contrato de la fuente; su código no es universal |
| Override / autorización | Decisión que modifica o exceptúa el flujo ordinario; puede introducir selección adicional |
| Buró | Fuente externa de información crediticia; sus scores, etiquetas y centinelas requieren diccionario y disponibilidad temporal |
| Score | Valor que ordena riesgo; su dirección y escala deben declararse. No es necesariamente una PD calibrada |
| Target / malo | Etiqueta de resultado con evento, umbral, ventana y disponibilidad definidos |
| Point-in-time | Construcción de datos usando únicamente información disponible en el momento de la decisión |
| Lineage / trazabilidad | Relación entre fuentes, versiones, transformaciones y artefactos finales |

## Tiempo, atraso y mora

| Término | Significado en este perfil |
|---|---|
| Cohorte / cosecha | Grupo por período de otorgamiento, habitualmente mes calendario |
| MOB | Months on book: edad desde el otorgamiento. Se declara si el mes inicial es 0 o 1 |
| Madurez | Cierre de la ventana de observación con fuente efectivamente completa para evaluar el target |
| Censura | Resultado todavía no observable completamente; no equivale a ausencia de evento |
| Atraso | Conteo o tasa de operaciones que cumplen un umbral de días de atraso en una ventana |
| Vencido acumulado | Importe de obligaciones vencidas acumuladas según componentes definidos |
| Moroso acumulado | Vencido acumulado menos pagos aplicados a esas obligaciones, según el contrato de datos |
| Mora | Índice monetario: suma de moroso sobre suma de vencido |
| Stock | Foto de un saldo o exposición a una fecha |
| Flujo | Importe ocurrido o acumulado durante un período definido |
| Vintage | Organización cohorte × edad de observación; facilita revisar madurez y proyectar evolución |
| Mora N+C | Índice sobre N cohortes en un corte calendario con C meses de colchón; no es una edad fija para todas las cohortes |
| Chain Ladder | Familia de métodos de proyección de triángulos; necesita hipótesis de desarrollo y validación propias |
| Cohorte sintética | Cohorte futura simulada bajo un escenario explícito |
| Deflactación | Expresar montos en una unidad monetaria de poder adquisitivo constante, declarando índice y mes base |

## Evaluación y pérdida

| Término | Significado en este perfil |
|---|---|
| KS por deciles | Máxima distancia acumulada entre buenos y malos en límites de los deciles acordados; KS canónico del perfil, en porcentaje |
| KS exacto | Distancia máxima entre distribuciones empíricas evaluada en todos los cortes; variante separada del KS por deciles |
| AUC | Área bajo ROC; se guarda en fracción y se declara orientación del score |
| Gini | Transformación `2*AUC−1`; necesita escala y convención declaradas |
| Calibración | Concordancia entre probabilidades estimadas y frecuencias observadas en una población y horizonte |
| PSI | Indicador de cambio de distribución respecto a una referencia con bins y suavizado fijados |
| WoE | Transformación supervisada de categorías o intervalos; se aprende con entrenamiento, no con las etiquetas de evaluación |
| IV | Resumen de separación por bins asociado a WoE; su tamaño no garantiza validez temporal o utilidad fuera de muestra |
| OOT | Out-of-time: evaluación sobre un período posterior al utilizado para desarrollar y seleccionar el modelo |
| Restricción de rango | Evaluación en un intervalo reducido del score, por ejemplo por cambios de aprobación; puede cambiar AUC/KS |
| Sesgo de selección | Diferencia entre la población observada y la población objetivo por mecanismos de inclusión |
| Leakage | Uso en desarrollo o evaluación de información que no habría estado disponible al decidir, o contaminación entre particiones |
| O/E | Observado sobre esperado; requiere definición del esperado, estandarización, unidades y exposición comparables |
| PD | Probabilidad de default para un evento, horizonte y población definidos |
| EAD | Exposición al momento del default, según la metodología correspondiente |
| LGD | Pérdida dado el default, con recuperos y criterios económicos o contables definidos |
| EL / ECL | Pérdida esperada / pérdida crediticia esperada; declarar si refiere a stock, flujo futuro y enfoque contable o económico |
| NIIF 9 | Marco contable relacionado con instrumentos financieros y pérdida crediticia esperada; su aplicación exige referencias vigentes del proyecto |

Las palabras compartidas no garantizan definiciones iguales. Cada intercambio de datos y cada comparación documenta las diferencias pertinentes.
