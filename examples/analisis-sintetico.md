# Ejemplo sintético: comparación de scores

Se quiere comparar dos scores sobre las mismas operaciones ficticias y un target binario maduro.

Contrato: una fila por operación; clave operacion_id; población sintética sin identificadores personales. El significado del target y el corte deben fijarse antes de medir; los valores del ejemplo no son resultados de cartera ni validación de modelos.

## Datos de demostración

```json
{
  "synthetic": true,
  "rows": [
    {"operacion_id": "op-a", "target": 0, "score_a": 820, "score_b": 760},
    {"operacion_id": "op-b", "target": 1, "score_a": 430, "score_b": 470},
    {"operacion_id": "op-c", "target": 0, "score_a": 690, "score_b": 710},
    {"operacion_id": "op-d", "target": 1, "score_a": 510, "score_b": 480}
  ]
}
```

Comprobar unicidad, faltantes, orientación y misma población. Este tamaño sirve para discutir el procedimiento; no acredita precisión estadística.

Si se incorpora una variable medida después de la decisión o del evento, el contrato temporal debe detectar leakage. Si los dos scores se evalúan sobre distintas cohortes, primero resolver la comparabilidad.
