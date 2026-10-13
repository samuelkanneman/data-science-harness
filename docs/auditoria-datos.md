# Auditoría de datos y análisis

Una ejecución correcta puede sostener una conclusión inválida. Esta guía revisa tanto la evidencia técnica como la población, el tiempo y el método que permiten interpretar un resultado. Adapta el checklist propio de auditoría a ciencia de datos general; los controles de dominio se agregan mediante [perfiles](perfiles/riesgo-crediticio/README.md).

## Alcance y forma de trabajo

El auditor aplica [el método](metodo.md), [las convenciones](convenciones.md) y el [rol centinela](roles/centinela.md). Trabaja en solo lectura, con revisión proporcional al riesgo y al alcance solicitado. No ejecuta extracciones, instalaciones o acciones externas sin autorización correspondiente; una revisión estática se informa como tal.

Antes de comprobar algo, identificar la pregunta, el resultado evaluado y las afirmaciones que pretende sostener. Para cada control registrar `verificado`, `con observaciones`, `no verificado` o `no aplica`, con evidencia o motivo. No marcar un control como aprobado por encontrar una instrucción escrita o un comando propuesto.

## 1. Pregunta y contrato del análisis

- [ ] La pregunta, destinatario y decisión que puede cambiar están definidos.
- [ ] Se distingue descripción, predicción, proyección, comparación y estimación causal.
- [ ] Unidad de análisis, clave, población objetivo, población observada, período y corte están declarados.
- [ ] Target o métrica tiene fórmula, unidades, orientación, umbral y ventana cuando correspondan.
- [ ] Inclusiones, exclusiones y denominadores están cuantificados; los cambios de definición están versionados.
- [ ] Las comparaciones usan definiciones compatibles o explican por qué no son directamente comparables.
- [ ] Supuestos de negocio y criterios de aceptación están registrados y tienen un responsable.

## 2. Fuentes, calidad y lineage

- [ ] Existe trazabilidad fuente → extracción → transformación → dataset → resultado, con versión o identificador de cada etapa.
- [ ] Las fuentes usadas pueden identificarse sin exponer credenciales ni datos personales en el entregable.
- [ ] Se verificó la cobertura real: períodos cargados, retención, cortes parciales, reconciliaciones y controles de magnitud adecuados.
- [ ] Se comprobaron esquema, tipos, unidades, separadores, encoding, zona horaria y valores centinela.
- [ ] Nulos, duplicados, rangos imposibles y outliers están medidos por período o segmento relevante; su tratamiento se justifica.
- [ ] Después de conversiones coercitivas se cuenta cuántos valores nuevos quedaron nulos.
- [ ] La clave es única para la unidad declarada o la repetición esperada está documentada.
- [ ] Los joins tienen cardinalidad prevista; se midieron filas sin match, duplicación y conservación de importes o conteos.
- [ ] Los filtros y agregaciones conservan el perímetro acordado y las tasas usan denominadores apropiados.

## 3. Disponibilidad temporal, target y leakage

- [ ] Se distingue tiempo del evento, registro, publicación y disponibilidad real para cada fuente relevante.
- [ ] Las variables podían conocerse en el momento de predicción; los joins históricos son point-in-time y no toman revisiones futuras sin justificación.
- [ ] El target está disponible con la ventana completa; su madurez se comprueba contra la fuente efectiva, además de la configuración.
- [ ] Observaciones censuradas, seguimiento incompleto o faltantes de etiqueta no se convierten en negativos por defecto.
- [ ] No hay variables post-evento, proxies del target, agregados futuros ni duplicados entre particiones.
- [ ] Imputación, escalado, bins, WoE, selección de variables y ajustes supervisados se aprenden solo con entrenamiento, dentro del fold cuando corresponda.
- [ ] Las dependencias por persona, operación, grupo o ventana superpuesta se consideran al partir y evaluar.

## 4. Partición, selección y evaluación

- [ ] Ajuste de parámetros, selección del modelo y evaluación final usan datos o procedimientos separados.
- [ ] El esquema de partición representa el uso esperado: temporal para pronósticos futuros, por grupos si hay dependencia, o aleatorio cuando se justifica independencia.
- [ ] Un OOT contiene períodos posteriores adecuados, con etiquetas maduras y sin reoptimizar sobre sus resultados.
- [ ] Validación cruzada, ventanas móviles y gaps se justifican según dependencia y horizonte; no se exigen a toda tarea por defecto.
- [ ] Se documenta cuántas variantes, cortes y parámetros se probaron; se evita presentar la mejor prueba como evidencia independiente.
- [ ] Los modelos comparados usan los mismos casos evaluables o explican diferencias de cobertura y población.
- [ ] Métricas, baseline y escala responden a la pregunta. Un descriptivo no requiere un baseline predictivo.
- [ ] Se consideran tamaños de muestra, prevalencia, incertidumbre y dependencia entre observaciones al interpretar diferencias.
- [ ] Se revisan mix, políticas de selección, cobertura, drift y restricción de rango antes de atribuir cambios al modelo.
- [ ] Calibración, discriminación y estabilidad se evalúan por separado cuando sean pertinentes.

## 5. Método, supuestos y proyecciones

- [ ] El método responde al problema y al volumen, frecuencia y horizonte disponibles; sus supuestos necesarios tienen evidencia.
- [ ] Los controles de estacionariedad, normalidad, multicolinealidad o residuos se aplican cuando el método o la inferencia los requieren; no se imponen a todos los modelos.
- [ ] Hay comparación con un baseline pertinente y backtesting cuando el objetivo es predictivo o de forecast.
- [ ] En forecast, el backtest reproduce horizonte, disponibilidad, revisiones de fuentes y variables exógenas conocibles al originar el pronóstico.
- [ ] Horizonte, escenarios y condiciones fuera de soporte están declarados; la proyección no se presenta como certeza.
- [ ] Predicciones respetan restricciones del dominio o explican excepciones; se revisa sensibilidad a supuestos y datos.
- [ ] Se distingue incertidumbre de parámetros, observación y escenario cuando afecta la decisión; los intervalos no se presentan con cobertura no comprobada.
- [ ] Residuos o errores se examinan por tiempo y segmento; patrones relevantes se explican y delimitan la utilidad.
- [ ] Un cambio de distribución no se interpreta automáticamente como cambio causal o como necesidad de reentrenar.

## 6. Causalidad y representatividad

- [ ] Las conclusiones descriptivas o predictivas no afirman efectos causales sin un diseño de identificación adecuado.
- [ ] Si se estima causalidad, se declara intervención o exposición, resultado, unidad, población, estimando y supuestos de identificación.
- [ ] Se verifica temporalidad y disponibilidad de contactos, tratamientos y controles; no se infiere efecto de una campaña solo por observar retorno posterior.
- [ ] Confusión, selección, cambios concurrentes y posibles efectos entre unidades se tratan según el diseño, con sensibilidad cuando corresponde.
- [ ] La población observada permite la generalización pretendida o se explicita el límite. Una muestra de aprobados no representa automáticamente a todos los solicitantes.
- [ ] Subgrupos relevantes tienen cobertura y tamaños suficientes; los riesgos de sesgo se documentan según contexto y obligaciones del proyecto.
- [ ] Una diferencia entre segmentos o una correlación no se presenta como atributo inherente del grupo sin analizar el mecanismo de observación.

## 7. Reproducibilidad y ejecución

- [ ] Los parámetros, entradas y catálogos usados están identificados mediante manifiesto, versión o hash, según el riesgo.
- [ ] Intérprete, dependencias y configuración efectiva están registrados; se puede reconstruir el entorno necesario.
- [ ] Aleatoriedad y orden de entrada están controlados donde influyen; la no determinación residual se cuantifica o explica.
- [ ] El pipeline tiene un comando o procedimiento reproducible, con errores visibles y controles de etapas.
- [ ] Las comprobaciones reportadas fueron ejecutadas con evidencia conservada; se diferencia test offline, prueba sintética y corrida real.
- [ ] El código de salida se complementa con logs, ausencia de errores relevantes y verificación de artefactos esperados.
- [ ] Cada salida tiene contenido y período correctos, fecha de modificación posterior a la corrida o una explicación verificable de reutilización.
- [ ] Los notebooks se guardaron con sus resultados antes de exportar informes; no se entrega una exportación de una corrida anterior.
- [ ] En corridas orquestadas se verifica ejecución real, consumo de tareas y generación de resultados; un schedule o API sano no equivale a éxito operacional.

## 8. Entregable, límites y gobernanza

- [ ] Cifras, fórmulas, gráficos y conclusiones del informe concuerdan con las fuentes y cálculos verificados.
- [ ] El entregable identifica período, corte, fuente, población, definición de las métricas y unidades.
- [ ] El contenido necesario está disponible al destinatario; una dependencia remota no impide revisar el resultado final.
- [ ] No hay secretos, datos personales o información corporativa fuera de su perímetro autorizado. Los ejemplos del harness son sintéticos.
- [ ] Supuestos, limitaciones, incertidumbre y validaciones pendientes son visibles junto a las conclusiones relevantes.
- [ ] Se distinguen implementación, validación offline y validación operacional; ninguna sustituye a otra.
- [ ] Para un uso continuo se documentan responsable, criterios de aprobación, población habilitada, monitoreo y respuesta a alertas.
- [ ] Se conserva historia de decisiones y se actualiza lo vigente sin convertir transcripciones privadas en documentación compartida.

## 9. Aplicación del perfil crediticio

Si el proyecto lo adopta, revisar [sus definiciones](perfiles/riesgo-crediticio/DEFINICIONES.md) y [sus errores transferibles](perfiles/riesgo-crediticio/GOTCHAS.md):

- [ ] Atraso por conteo y mora en dinero se rotulan con sus denominadores; no se mezclan stock y flujo.
- [ ] Mora N+C usa las cohortes calendario y cantidad exigidas; no se confunde con un MOB fijo.
- [ ] KS por deciles y KS exacto se distinguen; AUC, Gini y PSI declaran escala y método.
- [ ] El PSI conserva referencia, bordes, suavizado y cobertura; sus umbrales se interpretan como heurísticas.
- [ ] Refinanciaciones y códigos de buró se identifican por contrato y período, sin trasladar mapeos de otro proyecto.
- [ ] Montos nominales o reales, mes base, escenarios y alcance de PD/EAD/LGD se declaran.

## Dictamen con evidencia

| Dictamen | Condición |
|---|---|
| Aprobado | La evidencia cubre las afirmaciones y controles necesarios dentro del alcance auditado |
| Con observaciones | Hay límites o hallazgos que requieren aclaración o acción, pero las afirmaciones delimitadas siguen sostenidas |
| Rechazado | Un hallazgo material invalida una afirmación central o falta evidencia indispensable para el uso pretendido |

Ejemplos de hallazgos materiales: leakage confirmado, partición incompatible con el uso evaluado, target inmaduro reportado como final, multiplicación de importes por un join o resultado exportado desde otra corrida. No se usan umbrales universales de nulos, horizonte o tamaño muestral como rechazo automático; se justifica su impacto sobre la pregunta y la evidencia.

Cada hallazgo indica ubicación, hecho observado, impacto, evidencia, alcance y acción sugerida. Se consolidan duplicados y se distinguen problemas confirmados de sospechas. El auditor no corrige los archivos mientras emite el dictamen.

El cierre resume qué se auditó, con qué nivel de comprobación, cuáles afirmaciones quedan sostenidas, qué queda pendiente y quién debe resolverlo. Una revisión estática nunca certifica por sí sola conectividad, permisos efectivos, corrida de datos ni cumplimiento regulatorio.
