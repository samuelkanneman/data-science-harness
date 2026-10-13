# cosecha — cohortes, vintage y proyecciones

**Propósito:** medir y proyectar series por cohorte con perímetros comparables, conciliación, backtest y bandas de incertidumbre.

**Cuándo usar:** triángulos vintage, ventanas de mora, proyección de cartera o ventas, escenarios y experimentos de forecasting. Las corridas mensuales existentes pasan a [maquinista](maquinista.md).

## Contexto mínimo

Leer `AGENTS.md`, bitácora relevante, scripts vigentes y gotchas del destino. Aplicar [método](../metodo.md), [convenciones](../convenciones.md) y [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md).

## Procedimiento

1. Clasificar el pedido: lectura, corrida, nueva ventana o experimento. Reutilizar salidas y funciones vigentes; no sustituir un pipeline por una variante de legado.
2. Declarar cohorte, madurez, ventana, colchón, corte y perímetro. Para una nueva ventana, derivarla desde las definiciones y conciliar contra la referencia oficial.
3. Identificar censura, cohortes incompletas, cambios de codificación, refinanciaciones y quiebres de población antes de consolidar series.
4. En una proyección, preregistrar hipótesis, variantes, baseline y aceptación antes de la primera corrida. Reservar períodos de backtest y medir error por horizonte y cohorte.
5. Comparar contra un baseline naive o estacional. Usar bandas empíricas y medir cobertura; una banda dibujada sin backtest no expresa cobertura comprobada.
6. Registrar resultados y decisión. Una variante que no cumple el criterio preregistrado no se promueve.

## Reglas del perfil de riesgo

- Mora de flujo acumulado = suma de moroso dividida por suma de vencido. No sustituir por ratios de stock ni por promedio de índices.
- Mora 12+3 al corte M: cohortes de M−14 a M−3. Publicar cortes completos con `n_cohortes == ventana`; las demás ventanas siguen la definición N+M del perfil.
- Declarar si el perímetro excluye refinanciaciones o es total. Verificar que los segmentos formen una partición antes de sumarlos; un agregado general no es necesariamente suma de reportes segmentados.
- La conciliación exige explicar cualquier brecha contra el oficial; el mismo cálculo debe coincidir a la precisión acordada, sin ocultar diferencias mediante redondeo.
- Como límite del procedimiento vigente, el horizonte no supera el 50% del histórico. Una excepción necesita justificación y evaluación explícitas en el proyecto.
- No modificar runners, lógica ni parámetros de producción sin autorización para ese cambio. Respetar configuraciones compartidas y separación de entornos documentadas.

## Entrega

Serie principal con corte, métrica, cohortes y denominador; conciliación, error de backtest, cobertura y quiebres. Para mora, reportar errores en puntos porcentuales y cobertura del intervalo definido, por ejemplo IC80 si es el vigente.
