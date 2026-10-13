# ksauc — corrida periódica de KS/AUC

**Responsable:** [maquinista](../roles/maquinista.md). Diagnóstico metodológico: [juez](../roles/juez.md).

**Alcance:** ejecutar el pipeline vigente del destino. Este procedimiento no entrega un notebook ni comandos de un cliente particular; el catálogo y `AGENTS.md` resuelven rutas, intérprete, entradas, comando y salidas.

## Preparación

Leer [convenciones](../convenciones.md) y [definiciones de riesgo](../perfiles/riesgo-crediticio/DEFINICIONES.md). Confirmar período solicitado, madurez del target, población, orientación del score y autorización de corrida.

## Procedimiento

1. Anotar inicio y listar carpetas de período existentes. Elegir la correspondiente; si hay varias candidatas, resolver la ambigüedad. Verificar insumos de operaciones y transacciones según el pipeline.
2. Leer el contrato de parámetros permitidos. Normalmente comprende año, mes, nombre del período y carpeta de datos; confirmar campos exactos en el destino.
3. Editar solo esos parámetros y mostrar diff. Si el mes es numérico en YAML, guardar un entero sin cero inicial. No cambiar umbral, score, desempate, semilla ni salida.
4. Ejecutar con el runner o comando canónico y timeout documentado. Conservar log y controles; no reconstruir un flujo equivalente.
5. Regenerar el HTML después de guardar el notebook ejecutado. Si el pipeline exporta mientras el notebook aún no se guardó, hacer obligatoriamente el segundo pase documentado; no aceptar el HTML de la corrida anterior.
6. Verificar artefactos que deban regenerarse, período del título, contenido y cifras globales. Confirmar KS por deciles y AUC guardado como fracción, además de n y exclusiones. Un archivo conservado por idempotencia requiere evidencia según el contrato del destino.
7. Comparar contra un período compatible. Un movimiento mayor que tres puntos porcentuales de AUC o KS pasa a juez para revisar mix, dispersión, PSI y política antes de atribuir deterioro.
8. Entregar parámetros, duración, log, salidas y controles, y aplicar [cierre](cierre.md).

## Fallos

Capturar traceback y diagnóstico depurados. No modificar lógica para completar la corrida. Distinguir falta de datos, conexión y bug; una salida existente no demuestra éxito.
