# Errores transferibles del trabajo con datos

Selección adaptada del registro propio de errores; revisada el 2026-10-13. Los IDs `G-NNN` conservan la referencia histórica. La recomendación se volvió portable: no transporta hosts, esquemas, columnas corporativas, cifras de cartera ni códigos de clientes. Aplicar únicamente los casos pertinentes al proyecto.

## Datos, métricas y negocio

| Referencia | Error y consecuencia | Control transferible |
|---|---|---|
| G-022, G-023 | Una clave parcial se toma por identificador único; un join multiplica filas o importes | Declarar unidad y clave completa; medir multiplicidad antes del join y validar cardinalidad, conteos e importes después |
| G-024, G-035 | Refinanciaciones identificadas por un código que cambia entre períodos o archivos | Versionar el mapeo según contrato de datos; tratar nulos explícitamente y comprobar coherencia temporal del perímetro |
| G-025 | Un saldo de stock se usa como flujo acumulado | Declarar la naturaleza de cada importe y conciliar numerador y denominador con la misma definición |
| G-026 | Se promedian tasas de segmentos con distinto denominador | Agregar numeradores y denominadores; calcular la razón de sumas |
| G-027 | Se usa una fuente externa como si estuviera disponible en el mes que describe | Registrar fecha del evento, publicación y disponibilidad real; construir joins point-in-time según lo conocido al decidir |
| G-027 | Los importes o códigos especiales de una fuente se interpretan sin diccionario | Verificar unidades, códigos centinela, nulos y cambios de versión; no asumir convenciones de otra fuente |
| G-028 | Se da orden a una etiqueta nominal o se trata un centinela como score válido | Verificar semántica y cobertura; separar centinelas y usar una codificación compatible con la variable |
| G-029 | Menor atraso observado de un segmento seleccionado se interpreta como menor riesgo inherente | Explicar filtros y overrides; delimitar la población a la que se puede generalizar |
| G-030, G-031 | Una caída de AUC/KS se atribuye al modelo sin revisar cambios en aprobaciones y mezcla | Comparar cohortes maduras y mismo target; examinar cobertura, rango de score, política y mix |
| G-032 | Se calcula cobertura sobre un universo distinto del que se va a analizar | Medir faltantes por población objetivo, cohorte y canal; informar denominadores |
| G-036 | Se espera que la suma de segmentos concilie con un total construido con otro perímetro | Verificar igualdad de poblaciones, reglas, fechas y solapamientos antes de conciliar |

No hay un retraso externo fijo válido para todas las fuentes. Una demora histórica orienta un control; no sustituye la fecha real de publicación. Tampoco se exportan las codificaciones originales de refinanciación o score.

## Lectura y transformación

| Referencia | Error y consecuencia | Control transferible |
|---|---|---|
| G-040 | Un decimal localizado queda como texto y `to_numeric(coerce)` lo convierte en NaN | Declarar separador y decimal al leer; contar nulos previos y nuevos después de convertir; impedir que un target NaN se vuelva bueno |
| G-041, G-043 | Una decodificación permisiva tapa errores o un BOM contamina el encabezado | Aplicar el encoding del contrato; para el formato heredado, probar `utf-8-sig` y luego `cp1252` solo si falla; validar encabezados y texto |
| G-042 | Se cambia coma por punto sin interpretar el separador de miles | Parsear según el formato conocido, no con reemplazos globales; validar ejemplos y errores de conversión |
| G-044 | `pd.NA` se evalúa como booleano en una condición | Tratar faltantes explícitamente; probar las ramas con valores válidos y ausentes |
| G-045 | YAML produce tipos diferentes por escribir meses con cero inicial | Usar esquema y validar tipos al cargar; mes como entero en `1..12`, período como texto ISO |
| G-046 | Los empates impiden formar los cuantiles esperados | Documentar regla de empates y bins efectivos; para el KS de este perfil usar su especificación de jitter y `duplicates='drop'` |
| G-047 | El mismo código se ejecuta con otro entorno y cambian tipos o semántica | Declarar intérprete y dependencias; verificar el entorno que ejecutó la corrida |
| G-048 | Se construye un nombre de carpeta histórico que no existe o apunta a otro período | Usar el manifiesto de artefactos o seleccionar sobre rutas existentes; no adivinar nombres |
| G-049 | Un catálogo editable cambia sin quedar identificado en la corrida | Versionar la foto aprobada del catálogo y registrar su hash o versión; explicitar su actualización |

`utf-8-sig`, `cp1252`, separador `;` y decimal `,` describen un contrato de intercambio heredado. Otros formatos requieren su propio contrato; una importación no debe imponerlos sobre el archivo recibido.

## Extracción y ejecución

| Referencia | Error y consecuencia | Control transferible |
|---|---|---|
| G-003, G-009 | Literales ambiguos o un límite a medianoche excluyen registros del último día | Parametrizar fechas según motor; usar intervalos `[desde, hasta_exclusivo)` para timestamps y declarar zona horaria |
| G-006 | El driver convierte decimales con un locale incompatible | Diagnosticar en qué etapa falla la conversión; verificar tipos y precisión antes de adoptar un cast específico |
| G-008 | Espacios de relleno cambian filtros sobre etiquetas | Normalizar de acuerdo con el contrato y auditar cuántos valores cambian; no alterar texto libre indiscriminadamente |
| G-010, G-011 | Listas o joins exceden límites del motor o hacen una extracción impracticable | Revisar límites documentados y perímetro; particionar consultas autorizadas y validar la unión local |
| G-013, G-014, G-019 | Una fuente reciente o parcial se usa como historia completa | Verificar retención, máximos temporales y controles monetarios apropiados; un conteo de filas aislado no acredita completitud |
| G-061 | `jupyter` en PATH usa otro entorno | Invocar el módulo mediante el intérprete declarado y registrar la versión efectiva |
| G-067 | El formulario de un orquestador existe, pero sus parámetros fallan al ejecutar | Verificar parámetros válidos e inválidos y su serialización; el esquema solo no prueba la corrida |
| G-068 | Servidor sano, pero el proceso que toma tareas está detenido | Verificar consumo, estado y logs de la ejecución prevista antes de declarar éxito o crear duplicados |
| G-069 | Un schedule guardado no genera corridas por incompatibilidad de dependencias | Comprobar corridas efectivamente generadas; resolver en el entorno aislado y validar compatibilidad |

Los detalles de driver, aislamiento, casting y tamaño de lotes dependen del motor y del entorno. Este perfil mantiene consultas de DW solo `SELECT`; no prueba escrituras con rollback. Un cast a float puede perder precisión monetaria y requiere justificación en el contrato del proyecto.

## Entregables y seguridad

| Referencia | Error y consecuencia | Control transferible |
|---|---|---|
| G-060 | Un HTML se exporta desde un notebook que todavía contiene resultados anteriores | Guardar el notebook ejecutado antes de exportar o usar un segundo pase; comprobar contenido, período y `mtime` de cada artefacto |
| G-063 | Un HTML depende de un CDN inaccesible al destinatario | Empaquetar las dependencias necesarias para el contexto de entrega y verificar el artefacto final sin conexión cuando corresponda |
| G-080 | Credenciales quedan en código, notebooks o logs | Usar el mecanismo de secretos del entorno; revisar fuentes, salidas y diffs antes de publicar |
| G-081 | Datos personales viajan en un informe o ejemplo | Minimizar y usar ejemplos sintéticos; un reemplazo de identificadores no garantiza anonimización |

La fecha de modificación es evidencia de frescura, pero no prueba por sí sola que los datos sean correctos. Registrar período, contenido, logs, controles y, cuando corresponda, hashes. Cada nuevo error conserva causa, evidencia, corrección o pendiente y alcance; una sospecha no se registra como problema confirmado.

Referencias de uso: [definiciones](DEFINICIONES.md), [glosario](GLOSARIO.md) y [auditoría general](../../auditoria-datos.md).
