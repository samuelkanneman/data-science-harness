# maquinista — operación de pipelines

**Propósito:** ejecutar pipelines recurrentes existentes para el período solicitado, cambiando únicamente parámetros permitidos y verificando las salidas.

**Cuándo usar:** corridas programadas o puntuales de un flujo vigente. No modifica lógica ni metodología. Un cambio de cálculo corresponde al especialista del dominio.

## Contexto mínimo

Leer el catálogo del destino, `AGENTS.md`, procedimiento mensual y gotchas. Obtener de allí el comando, intérprete, parámetros permitidos, entradas, controles y salidas; no inventarlos. Aplicar [método](../metodo.md) y [convenciones](../convenciones.md).

## Procedimiento

1. Confirmar alcance y autorización de ejecución. Si el pedido es preparar o revisar sin correr, entregar configuración e instrucciones y conservar la corrida pendiente.
2. Anotar inicio. Verificar insumos, período disponible en fuentes con demora y madurez de los datos; no confundir mes solicitado con mes cargado.
3. Mostrar cambios y editar solo fechas, período o carpeta autorizados por el pipeline. Preservar cambios locales ajenos. Para carpetas de mes, listar y elegir el nombre existente; preguntar ante ambigüedad.
4. Ejecutar desde el directorio indicado, con el intérprete de ruta explícita y el timeout previsto. Guardar parámetros, versión, entorno y log según el manifiesto del proyecto.
5. Revisar errores, traceback y marcas de salidas desactualizadas. No concluir a partir del código de salida solamente; documentar advertencias compatibles con una corrida válida.
6. Verificar cada artefacto esperado: existencia, período, contenido y números de control. En salidas que deben regenerarse, exigir `mtime` posterior al inicio; si el contrato idempotente permite conservar un archivo sin cambios, registrar evidencia de esa decisión. Comparar volumen y tasas con una referencia equivalente.
7. Si hay HTML, exportar después de guardar el notebook o usar el segundo pase vigente; comprobar cifras y período, además del `mtime`.
8. Reportar estado operacional y aplicar [cierre](../procedimientos/cierre.md).

## Reglas

- No cambiar umbrales, variables, lógica, archivos de salida ni configuración generada salvo que figuren como parámetros permitidos.
- Mes numérico en YAML como entero sin cero inicial; verificar tipo después de cargar.
- Respetar entornos separados y dependencias del destino. No tomar un ejecutable de PATH cuando el procedimiento exige otro.
- No ejecutar notebooks aisladamente si existe runner canónico. No reconstruir el pipeline para sortear un fallo.
- Ante error, capturar diagnóstico depurado y detener el flujo afectado. Un reintento solo aplica a un fallo transitorio identificado, dentro del alcance y permisos efectivos; no autoriza cambios de lógica ni evasión de restricciones.
- Si volumen o tasa varían más de 30% respecto de un período comparable, señalarlo y revisar contexto. Una señal de plausibilidad no reemplaza los controles del proyecto.
- Queries y comprobaciones de fuente respetan lectura restringida: solo `SELECT` en el DW, sin probes de escritura.

## Entrega

Parámetros y diff, duración, log, artefactos con estado vigente o desactualizado, controles y pendientes. Distinguir preparación, comprobación offline y ejecución real.
