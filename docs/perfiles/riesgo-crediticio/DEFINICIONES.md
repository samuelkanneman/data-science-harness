# Definiciones del perfil de riesgo crediticio

Especificación portable de la metodología propia. Revisada: 2026-10-13. Solo aplica cuando el proyecto adopta [este perfil](README.md); los desvíos se justifican, versionan y rotulan. Una coincidencia de nombre no hace comparables dos métricas.

## 1. Unidad de análisis y target

La clave debe identificar la unidad declarada: solicitud, operación, cliente o cliente-período. Una clave de negocio puede ser compuesta; antes de guardar o unir datos se verifica unicidad o se explica la multiplicidad esperada.

Cada target binario se escribe de forma completa:

```text
malo = atraso_max en <ventana de observación> >= <umbral> días
```

Por ejemplo, `>= 60 días durante una ventana de 6 meses` y `>= 90 días durante una ventana de 12 meses` son targets distintos. Son ejemplos de definición, no un default ni una política de crédito.

- Se declara el inicio y cierre de la ventana, la convención de MOB y el momento de disponibilidad de la etiqueta.
- Comparar cohortes a una misma ventana de observación evita que las más antiguas parezcan peores por tener más seguimiento.
- Una etiqueta faltante o un período incompleto no es un caso bueno. Se informa su volumen, motivo y tratamiento.
- La madurez se verifica contra el cierre de la ventana y contra la cobertura real de la extracción. Cambiar la fecha configurada no vuelve madura una foto parcial guardada antes.
- La población de evaluación puede diferir de la de aplicación; se explican las consecuencias y las exclusiones.

## 2. Atraso, mora y agregación

En este perfil, **atraso** es una medición por conteo de operaciones y **mora** es un índice en dinero. Esta elección editorial no obliga a otros dominios a usar el mismo vocabulario.

```text
tasa_atraso = suma(operaciones_malas) / suma(operaciones_evaluables)
moroso_acumulado = vencido_acumulado − pagado_aplicado_al_vencido
indice_mora = suma(moroso_acumulado) / suma(vencido_acumulado)
```

Se define qué componentes entran en vencido y pagado, su signo, unidad, fecha y conciliación. La fórmula no autoriza a usar cualquier columna de pagos. Un saldo de stock y un flujo acumulado responden preguntas distintas.

Al agregar segmentos, se divide la suma de numeradores por la suma de denominadores. No se usa la media simple de tasas, salvo que la pregunta sea explícitamente el promedio de tasas entre grupos y se lo rotule así. El denominador cero produce una métrica no definida, no una tasa cero.

## 3. Mora N+C: cohortes por calendario

Se usa `T` para el mes de corte, `N` para el número de cohortes de otorgamiento y `C` para el colchón de meses. La notación evita confundir el mes de corte con el colchón.

```text
cohortes = T − (N + C − 1), ..., T − C      # extremos inclusivos
mora_N_C(T) = suma(moroso en T) / suma(vencido en T)
```

La agregación se realiza sobre esas cohortes, en la foto del mes `T`. Es una diagonal calendario del triángulo vintage; las cohortes tienen distintas edades. No equivale al atraso observado a un MOB fijo ni al punto final de una curva proyectada.

| Métrica | Cohortes incluidas | Cantidad exigida |
|---|---|---|
| Mora 12+3 | `T−14 .. T−3` | 12 |
| Mora 6+3 | `T−8 .. T−3` | 6 |
| Mora 13+1 | `T−13 .. T−1` | 13 |
| Mora 26+1 | `T−26 .. T−1` | 26 |

Ejemplo sintético: corte `2026-03`, mora 12+3 → cohortes `2025-01 .. 2025-12`. Un corte requiere todas las cohortes esperadas y cobertura monetaria completa; contar cohortes no demuestra que la fuente haya terminado de cargar.

El proyecto documenta si el mes de otorgamiento cuenta como MOB 0 o MOB 1. La definición por meses calendario prevalece ante convenciones distintas. Una serie heredada llamada `12+3` que mida otra cosa conserva un rótulo explícito y no se mezcla con esta serie.

## 4. KS por deciles y KS exacto

Para la comparabilidad de este perfil, **KS canónico** significa KS por deciles y se informa en porcentaje.

1. Usar filas evaluables con target binario y score válido, informando exclusiones; se necesitan ambas clases.
2. Orientar el score para que valores más altos indiquen mejor calidad crediticia.
3. Aplicar jitter `uniform(-0.01, 0.01)` con `numpy.random.RandomState(42)` sobre ese score para desempatar, conservando orden reproducible de las filas.
4. Formar 10 buckets mediante `pandas.qcut(..., q=10, duplicates='drop')`.
5. Ordenar los buckets por su score mínimo ascendente; el decil 1 es el más riesgoso.
6. Calcular `KS_deciles_pct = 100 * max(abs(acum_malos − acum_buenos))` en los límites de los buckets.

`acum_malos` y `acum_buenos` son proporciones acumuladas dentro de cada clase. Se informa cuántos buckets quedaron, la cantidad por bucket, el jitter y la versión del procedimiento. La amplitud de jitter está expresada en puntos del score original; no se traslada directamente a una probabilidad en `[0,1]` sin definir y rotular una variante.

El KS exacto sobre las distribuciones empíricas, por ejemplo `scipy.stats.ks_2samp`, evalúa todos los cortes posibles. Otra partición por ranking también es una variante. Se rotulan como tales, con su escala, y no se comparan como si fueran el mismo KS canónico. El jitter se usa para el agrupamiento acordado; no se modifica silenciosamente el score publicado ni otras métricas.

## 5. AUC, Gini y comparación de scores

```text
AUC = roc_auc_score(malo, probabilidad_de_malo)
AUC = roc_auc_score(malo, −score)             # si más score significa mejor
Gini = 2 * AUC − 1
```

- AUC se guarda como fracción `[0,1]`; puede mostrarse como porcentaje con rótulo y escala explícitos. Gini también declara su escala.
- Una transformación estrictamente monótona en la dirección correcta conserva el ranking y el AUC en aritmética exacta; no convierte el score en una probabilidad calibrada. Saturación y empates numéricos requieren control.
- Se informan nulos, clases ausentes y tamaño de cada clase. Con una sola clase, AUC y KS quedan no definidos.
- Para comparar modelos sobre las mismas operaciones, se conserva la intersección de casos y el mismo target, ventana y corte. Se informa la cobertura perdida por esa intersección.
- La comparación de AUC debe considerar dependencia entre scores y unidad de muestreo; una comparación pareada puede usar DeLong bajo sus supuestos. La incertidumbre no reemplaza la revisión de población y madurez.

**Decil 1 = más riesgoso**: menor score si más alto es mejor, o mayor probabilidad de malo. Los deciles calculados de nuevo por cohorte describen su ranking; las bandas fijas del desarrollo permiten comparar calibración con cortes constantes.

## 6. PSI: especificación y población de referencia

El PSI mide un cambio de distribución; no demuestra deterioro predictivo, calibración correcta ni causalidad.

```text
PSI = suma((proporcion_nueva − proporcion_ref)
           * log(proporcion_nueva / proporcion_ref))
```

La especificación del perfil, derivada de su función de monitoreo original, es:

1. Elegir y versionar una población de referencia; declarar período, perímetro y dirección del cambio.
2. Calcular 10 bins por cuantiles de la referencia, con extremos reemplazados por `−inf` y `+inf`.
3. Deduplicar bordes repetidos; registrar bordes y cantidad efectiva de bins.
4. Contar referencia y población nueva usando los mismos bordes (`numpy.histogram`); dividir cada conteo por el tamaño de su población evaluable.
5. Recortar cada proporción a un mínimo de `1e-6`, sin renormalizar después, y aplicar la fórmula.

Los datos deben ser numéricos finitos y las poblaciones no vacías. Se registra cobertura y tratamiento de faltantes antes de calcular; excluir nulos no debe ocultar un cambio en su frecuencia. Una referencia constante o bins degenerados necesita diagnóstico adicional, aunque el PSI devuelva un valor pequeño.

Las bandas históricas de interpretación son `< 0.10` estable, `0.10 .. 0.25` cambio moderado y `> 0.25` cambio fuerte. Son heurísticas del perfil, no límites universales de aprobación. Investigar volumen, composición y cobertura antes de decidir una acción. Cambiar bins, referencia, suavizado o exclusiones cambia la métrica; se versiona y no se mezcla la serie.

## 7. WoE, IV y categorías

WoE representa categorías o intervalos mediante la distribución del target. En la convención `malo=1`, `bueno=0` y WoE positivo hacia buenos:

```text
dist_buenos_bin = buenos_bin / total_buenos
dist_malos_bin = malos_bin / total_malos
WoE_bin = log(dist_buenos_bin / dist_malos_bin)
IV = suma((dist_buenos_bin − dist_malos_bin) * WoE_bin)
```

Las proporciones sin soporte requieren una regla de suavizado o tratamiento definida; no se aplica la expresión con divisiones por cero. El proyecto declara si usa esta convención o su inversa, además de librería, suavizado, tratamiento de nulos y desconocidos, tamaño mínimo de bin y restricciones de monotonicidad.

- El binning, WoE y selección por IV se ajustan únicamente con la partición de entrenamiento y dentro de cada fold cuando hay validación cruzada.
- Se aplican los cortes y mapeos aprendidos a validación, test y OOT; usar sus etiquetas para recomputarlos es leakage.
- Una etiqueta de un buró no es ordinal por su nombre o por un código numérico. Se verifica su semántica; una categoría nominal requiere codificación adecuada, sin imponer un orden inexistente.
- Un IV excepcionalmente alto exige revisar disponibilidad temporal, variables derivadas del target y errores de partición. No prueba por sí solo que la variable sea válida o inválida.

Los umbrales de IV y parámetros de binning se eligen y validan para el proyecto; este perfil no los convierte en políticas universales.

## 8. Perímetro, refinanciaciones y selección

Cada resultado declara el perímetro: por ejemplo, `sin refinanciaciones` o `total, con refinanciaciones`. También declara otras exclusiones y sus cantidades.

La identificación de refinanciaciones pertenece al contrato de la fuente. Se verifica con responsables, campos, valores nulos y regímenes históricos de carga. No se presume que `0`, un nulo, una letra o una etiqueta tengan el mismo significado entre fuentes o períodos. Un cambio de codificación puede generar un salto artificial en la serie.

Se evalúan refinanciaciones separadamente cuando su proceso y riesgo difieren, y se explica cualquier consolidación. Para comparar series se acuerda el mismo perímetro; no se adopta una exclusión porque otro proyecto la use.

La cartera otorgada, autorizada o sobreviviente es una muestra seleccionada. Su atraso observado no identifica automáticamente el riesgo de todos los solicitantes ni de los rechazados. Ante una caída de AUC/KS se revisan mix, cambios de política, overrides, cobertura y restricción de rango antes de atribuirla al modelo.

## 9. Montos, proyecciones y pérdida esperada

- Para comparar montos en el tiempo, declarar moneda, unidad, inflación, índice, mes base y cobertura. Separar valores nominales y reales.
- Un forecast conserva horizonte, población, escenario, método de validación y límites. La incertidumbre se presenta cuando la decisión la necesita.
- PD, EAD y LGD dependen del evento, horizonte y población definidos. `PD * EAD * LGD` es una descomposición ilustrativa; una estimación contable o económica necesita su metodología, descuento, dependencia, escenarios y conciliación.
- Distinguir pérdida sobre stock de exposiciones y pérdida de flujo futuro; no compararlas por compartir la sigla EL/ECL.
- Este paquete no fija PD, LGD, recupero, coeficientes ni una interpretación normativa. El proyecto necesita sus fuentes y criterios vigentes.

## Procedencia y control de cambios

Adaptación de las definiciones compartidas de la metodología propia: targets, agregación, N+C, métricas, perímetro y montos. La especificación de KS y PSI se contrastó con sus implementaciones de referencia al preparar esta exportación. Los campos de fuentes privadas y las convenciones exclusivas de clientes se eliminaron.

Las decisiones nuevas se registran en el proyecto y en la bitácora del harness cuando cambian este perfil. Revisar también [los errores transferibles](GOTCHAS.md) y [la auditoría general](../../auditoria-datos.md).
