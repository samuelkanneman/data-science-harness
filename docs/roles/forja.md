# forja — construcción y explicación de modelos

**Propósito:** diseñar, entrenar y documentar modelos reproducibles, con hipótesis y criterios de éxito previos a la corrida.

**Cuándo usar:** construir o reentrenar modelos, experimentar con variables, comparar variantes durante su desarrollo y explicar predicciones. La extracción es de [veta](veta.md); la validación independiente y el monitoreo son de [juez](juez.md).

## Contexto mínimo

Leer `AGENTS.md`, historial de experimentos e implementaciones vigentes del destino. Aplicar [método](../metodo.md), [convenciones](../convenciones.md) y, para scores o PD, [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md).

## Procedimiento

1. Escribir hipótesis, población, target, criterio de éxito y baseline antes de entrenar. Revisar intentos anteriores para no repetir experimentos descartados sin nueva evidencia.
2. Separar ajuste, selección y evaluación. En riesgo crediticio, dividir temporalmente por cohortes y reservar una evaluación fuera de tiempo (OOT) madura; un split aleatorio no decide la promoción.
3. Preparar variables y transformaciones usando solo información disponible al decidir. Ajustar preprocesamiento con entrenamiento; documentar fechas ancla y rezagos de fuentes externas.
4. Entrenar baseline y variante con datos, semillas, entorno y parámetros registrados. En scorecards, investigar IV alto, revisar signos y usar monotonía cuando tenga sentido de negocio.
5. Evaluar con métodos vigentes, reportando resultados de entrenamiento, validación y OOT. Comparar sobre poblaciones y targets compatibles; incluir estabilidad por cohorte e incertidumbre del delta.
6. Explicar el comportamiento con coeficientes o atribuciones pertinentes. Contrastar la explicación con el negocio; una explicación plausible no certifica validez.
7. Registrar resultado, decisión y siguiente paso. Proponer promoción solo con evidencia suficiente y revisión independiente.

## Reglas

- Cohortes maduras para el target y ventana fija. No usar datos posteriores al evento ni una fuente publicada después de la decisión histórica.
- Declarar población de entrenamiento y límites de extrapolación. Un modelo construido con casos aprobados no representa automáticamente a todos los solicitantes.
- Cuando se comparen montos de distintos períodos, declarar ajuste por inflación y mes base.
- Investigar un IV mayor a 0,5 antes de admitir la variable; el umbral es una señal de revisión, no una prueba de leakage.
- Conservar un registro de datos, variables, parámetros, métricas, entorno y artefactos de cada experimento.
- Promover una versión requiere autorización para esa acción, respaldo anterior, metadata con hashes, variables, umbrales, fecha y población, y plan de monitoreo con juez. Reutilizar la autorización ya concedida para ese alcance.
- No cambiar producción como efecto lateral de un experimento; no mezclar entornos sin comprobar compatibilidad.

## Entrega

Baseline frente a variante, particiones, exclusiones, métricas, explicación, artefactos y decisión propuesta. Distinguir el modelo entrenado de la versión validada y de la versión desplegada.
