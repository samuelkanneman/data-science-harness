# Perfil de riesgo crediticio

Este perfil agrega definiciones y controles para analizar operaciones de crédito, validar scores y proyectar cartera. Es una extensión opcional de [la metodología general](../../metodo.md): sus ventanas, métricas y términos no son reglas para toda la ciencia de datos.

## Cuándo usarlo

- La unidad de análisis es una solicitud, operación, cliente o cohorte crediticia.
- Se evalúa atraso, mora monetaria, un score, estabilidad poblacional, una proyección vintage o pérdida esperada.
- El proyecto necesita un lenguaje compartido para comparar resultados crediticios.

El proyecto que adopta este perfil lo declara en su `AGENTS.md` y completa su propio contrato de datos y análisis. Una pregunta descriptiva no necesita activar todos los roles.

## Qué leer

| Archivo | Uso |
|---|---|
| [DEFINICIONES.md](DEFINICIONES.md) | Targets, tasas, ventanas N+C, KS, AUC, PSI, WoE y alcance de pérdida esperada |
| [GOTCHAS.md](GOTCHAS.md) | Errores transferibles observados en el trabajo de datos |
| [GLOSARIO.md](GLOSARIO.md) | Vocabulario del perfil |
| [Auditoría de datos](../../auditoria-datos.md) | Comprobaciones generales y dictamen con evidencia |
| [Convenciones](../../convenciones.md) | Formatos, ejecución y trazabilidad del paquete |

## Contrato mínimo de cada proyecto

1. Unidad de análisis, clave y relación entre solicitud, cliente y operación.
2. Población objetivo, criterios de inclusión, exclusiones y tratamiento de refinanciaciones.
3. Target con umbral, ventana, regla de madurez y tratamiento de observaciones incompletas.
4. Período, fecha de corte, cobertura efectiva de las fuentes y disponibilidad de cada variable al decidir.
5. Convención de MOB, importes, unidades monetarias, flujo o stock y mes base si se deflacta.
6. Método y versión de cada métrica, dirección del score, manejo de empates y población usada en cada comparación.
7. Alcance de las conclusiones, controles observados y validaciones pendientes.

## Límites de esta exportación

Las definiciones provienen de la metodología propia de trabajo, adaptadas para uso portable y revisadas el 2026-10-13. Se conservan identificadores de errores históricos como referencia editorial; los documentos de origen no son necesarios para usar este perfil.

El paquete no contiene esquemas corporativos, consultas a fuentes privadas, nombres de clientes, políticas de aprobación, coeficientes de modelos, valores de LGD ni datos de cartera. Tampoco define cómo una empresa identifica refinanciaciones: esa regla debe verificarse en el contrato de la fuente y en cada período.

Adoptar el perfil no certifica un modelo, una conexión o un informe. La aplicación necesita evidencia del proyecto de destino. Para otro dominio se crea otro perfil y se conservan los controles generales del harness.
