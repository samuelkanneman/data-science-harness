# vintage — corrida de cohortes y proyecciones

**Responsable:** [maquinista](../roles/maquinista.md). Dominio: [cosecha](../roles/cosecha.md).

**Alcance:** ejecutar un pipeline vigente de vintage, ventanas de mora o ventas. `AGENTS.md`, catálogo y procedimiento mensual del destino definen variantes, runners, entornos, parámetros y salidas.

## Preparación

Leer [convenciones](../convenciones.md) y [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md). Confirmar producto, ventana, colchón, período, corte, perímetro y autorización de corrida.

## Procedimiento

1. Anotar inicio. Elegir la variante vigente y comprobar fuente disponible y madurez. No mezclar general sin refinanciaciones, total y segmentos.
2. Leer el contrato de parámetros permitidos. Editar únicamente fechas, meses o corte que admita esa variante; mostrar diff y conservar lógica y configuración compartida.
3. Usar una comprobación previa sin corrida solo si existe y se verificó su comportamiento. Un nombre como `--check` no garantiza ausencia de efectos laterales.
4. Ejecutar con el runner e intérprete indicados. Si extracción y proyección usan entornos distintos, conservar la secuencia y no trasladar código entre ellos sin comprobar compatibilidad.
5. Verificar informes y tablas: existencia, `mtime`, período, cifras y marcas de desactualización. Si el HTML se generó antes de guardar el notebook, usar el segundo pase local documentado.
6. Comprobar cohortes completas: `n_cohortes == ventana`. Para mora 12+3 al corte M, la referencia es M−14..M−3; agregar mediante sumas de moroso y vencido.
7. Comparar el último corte contra un período equivalente. Señalar quiebres de codificación, refinanciaciones, población y series; revisar que los segmentos puedan sumarse antes de consolidar.
8. Entregar parámetros, log, salidas, controles y pendientes; aplicar [cierre](cierre.md).

## Límites

No ejecutar notebooks sueltos si existe runner. No cambiar empuje de diagonal, modelos, configuraciones inyectadas ni parámetros metodológicos durante la corrida. Todo cambio de lógica pasa a cosecha dentro de un alcance autorizado.
