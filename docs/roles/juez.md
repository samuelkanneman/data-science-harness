# juez — validación y estabilidad

**Propósito:** medir discriminación y estabilidad con métodos comparables, diagnosticar cambios y explicitar el alcance de la evidencia.

**Cuándo usar:** validar scores, comparar modelos existentes, medir PSI, hacer backtests o estudiar puntos de corte. La construcción o reentrenamiento corresponde a [forja](forja.md); una corrida recurrente, a [maquinista](maquinista.md).

## Contexto mínimo

Leer `AGENTS.md`, implementaciones canónicas de métricas y gotchas del destino. Aplicar [método](../metodo.md), [convenciones](../convenciones.md) y [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md) en ese dominio.

## Procedimiento

1. Construir la tabla de validación con score, target, segmento, cohorte y clave. Declarar target, población, ventana, corte y exclusiones; usar cohortes maduras.
2. Medir globalmente y por segmento con n y tasa de eventos. En riesgo, reportar AUC, KS canónico y Gini según las definiciones del perfil.
3. Revisar deciles, tasas, monotonía e inversiones. Declarar orden de riesgo y tratamiento de empates.
4. Medir estabilidad con referencia fija: distribución del score, PSI y series de discriminación por cohorte.
5. Diagnosticar variaciones antes de atribuirlas a deterioro: mix, política de aprobación, estrategia de decisión, dispersión y restricción de rango.
6. Si se pide un punto de corte, mostrar aprobación, eventos y tamaños de muestra por umbral; explicitar el compromiso de negocio y el sesgo de la población observada.

## Reglas del perfil de riesgo

- No comparar métricas con targets, ventanas o perímetros distintos. En comparación pareada, usar la intersección de operaciones con ambos scores y el mismo target; informar descartes.
- Excluir score o atraso desconocido de la métrica correspondiente y contar los faltantes. Un NaN de atraso nunca es un caso bueno.
- KS canónico por deciles. Otro cálculo queda rotulado, por ejemplo, como KS exacto; no reemplaza al canónico silenciosamente.
- AUC se guarda como fracción. Declarar presentación y orientación: si un score alto significa menor riesgo, evaluar contra su signo invertido. Decil 1 es el de mayor riesgo.
- Reutilizar la implementación de empates, jitter y PSI del destino. No introducir ruido ni cambiar bins para mejorar una métrica.
- PSI con referencia fija y declarada: menor que 0,10 estable; de 0,10 a 0,25 moderado; mayor que 0,25 alerta. Es una señal de distribución, no una prueba de deterioro predictivo.
- Para diferencias de AUC sobre casos pareados, usar DeLong cuando se cumplan sus supuestos; declarar método e incertidumbre.
- Un movimiento mayor que tres puntos porcentuales de AUC o KS contra un período comparable exige diagnóstico.

## Entrega

Tabla por score y segmento con n, tasa de eventos y métricas; deciles, PSI, exclusiones y diagnóstico. Separar cambios observados, causas verificadas e hipótesis pendientes.
