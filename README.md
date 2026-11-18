# AI_Surca

Modelo de estimación de demanda de Surca. Un script que corre una vez al día: lee los pedidos de PostgreSQL y guarda en la tabla `estimaciones` cuánto se espera vender de cada producto en las próximas 2 semanas.

**Tecnologías:** Python · pandas · scikit-learn · PostgreSQL (`psycopg`)

> Los datos de entrenamiento son **simulados**. No son pedidos reales.

## Cómo correrlo

```bash
python -m venv .venv
.venv\Scripts\activate          # en Windows
pip install -r requirements.txt
cp .env.example .env
pytest
```

## Estructura

```
src/surca_ai/
  constantes.py     semanas a estimar y aviso de datos simulados
tests/              pruebas con pytest
data/               datos simulados generados (no se suben a git)
```

## Plan

1. Generar datos simulados de pedidos (estacionalidad, ruido).
2. Entrenar una regresión con scikit-learn.
3. Evaluar con MAE y RMSE contra una línea base: el promedio de semanas anteriores.
4. Escribir las estimaciones en la tabla `estimaciones` de la base de datos del backend.
