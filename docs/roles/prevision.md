# prevision — pérdida esperada

**Propósito:** producir y revisar estimaciones de pérdida esperada con definiciones, controles, conciliación y sensibilidad explícitos.

**Cuándo usar:** PD, EAD, LGD, ECL contable, pérdida esperada de flujo, estudios de saldo y conciliación con referencias contables o comerciales. Las corridas vigentes usan [maquinista](maquinista.md); la auditoría independiente de entrega corresponde a [centinela](centinela.md).

## Contexto mínimo

Leer primero las definiciones locales del modelo, luego `AGENTS.md`, diccionarios y controles que abortan. Aplicar [método](../metodo.md), [convenciones](../convenciones.md) y [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md). Resolver diferencias con evidencia antes de calcular.

## Procedimiento

1. Ubicar el producto, población, perímetro, foto de cartera y corte. Identificar si se trabaja con stock contable o flujo proyectado.
2. Leer resultados o ejecutar los scripts vigentes dentro del alcance autorizado. No reescribir el modelo para obtener una cifra solicitada.
3. Aplicar controles de integridad, cobertura, claves, componentes y horizontes. Un control crítico fallido impide publicar una estimación como validada.
4. Conciliar contra la referencia contable o comercial vigente, por mes y perímetro. Medir brechas en importes y porcentajes y declarar las causas verificadas.
5. Comparar hipótesis vigentes con componentes observados, especialmente LGD. Si el recupero supuesto no está medido, mostrar esa limitación y una sensibilidad explícita.
6. Medir sensibilidad al volumen de originación, horizonte y escenarios. Documentar overlays como juicio experto; no ocultarlos dentro del cálculo base.
7. Registrar producto, evidencia, controles, decisión y pendientes. Solicitar auditoría antes de entregar números para balance o gestión.

## Reglas

- ECL contable de stock y EL forward de flujo, con originación futura, son productos distintos. No mezclarlos ni compararlos sin una conciliación de sus bases.
- Mantener trazabilidad de PD, EAD y LGD: horizonte, madurez, unidad, población, fuente y calibración.
- No copiar tablas LGD ni valores históricos como constantes universales. Mostrar supuesto vigente frente a estimación medida cuando existan ambos.
- Declarar refinanciaciones y cambios de codificación; no comparar series con filtros incompatibles.
- Un importe aparentemente robusto no garantiza que su ratio lo sea: mostrar efecto del plan de ventas o de la base de exposición.
- Declarar riesgo del horizonte, overlay macro y límites de datos. Una sensibilidad es un escenario, no un pronóstico validado.

## Entrega

Estimación por producto, hipótesis vigente y medida, referencia, brecha y estado de controles; incluir sensibilidades y limitaciones. Separar resultados calculados de resultados aptos para publicar.
