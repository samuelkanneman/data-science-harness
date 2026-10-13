# Evaluaciones y límites

Hay tres comprobaciones diferentes.

## Estructura

scripts/validar_repo.py comprueba inventario, frontmatter de envoltorios, enlaces locales, portabilidad y señales concretas de contenido excluido. Las pruebas de tests verifican que detecte casos adversos.

Una comprobación estructural no demuestra calidad de las instrucciones ni ausencia de toda información sensible. Requiere lectura del contenido antes de publicar.

## Comportamiento offline

[evals/casos.json](../evals/casos.json) contiene pedidos y criterios observables. Están diseñados para probar selección, autorización, coherencia de definiciones y honestidad de la evidencia.

Ejecutar cada caso en un entorno aislado sin DW, con los mismos artefactos sintéticos. Registrar herramienta, versión, modelo, contexto cargado, respuesta y efectos observados. Un evaluador independiente revisa los criterios. Comparar con y sin la skill cuando se quiera medir su aporte, manteniendo el resto constante y repitiendo casos para controlar variabilidad.

El archivo contiene escenarios, no resultados. No hay un runner de modelos ni evaluaciones de agentes ejecutadas en esta primera preparación.

## Operación real

Requiere proyecto, permisos, fuentes disponibles, período y corte. Observar integridad, salidas, frescura y coherencia con el contrato. Los fixtures y las pruebas unitarias no acreditan esta etapa.

Un resultado crítico pasa por el [auditor](roles/centinela.md). Los hallazgos incluyen evidencia, alcance e impacto; el acuerdo entre revisores no sustituye la verificación.
