# Numerical Methods Fullstack

Aplicación web para ejecutar métodos numéricos clásicos: ecuaciones de una variable, sistemas lineales iterativos e interpolación.

- **Backend:** Python + FastAPI + NumPy + SymPy. Algoritmos implementados a mano (uno por archivo).
- **Frontend:** HTML/CSS/JS estático servido por el mismo servidor. Solo maneja entrada, validación y graficación (Plotly + mathjs); el cálculo numérico vive completamente en el backend.

## Cómo ejecutar

```bash
cd backend-python
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Abre http://localhost:3000 — el mismo servidor sirve el frontend y la API.

Alternativa con recarga automática durante desarrollo:

```bash
uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

> Si ves "address already in use", libera el puerto 3000:
>
> ```bash
> lsof -ti:3000 | xargs kill -9    # macOS / Linux
> ```

## Estructura

```text
backend-python/
  main.py                          App FastAPI y rutas
  utils.py                         Parser SymPy, derivadas, eliminación gaussiana
  requirements.txt
  methods/
    single_variable/               Un archivo por algoritmo
      bisection.py
      false_position.py
      fixed_point.py
      newton_raphson.py
      secant.py
      multiple_roots.py
      compare.py
      common.py
    linear_systems/
      jacobi.py
      gauss_seidel.py
      sor.py
      compare.py
      common.py
    interpolation/
      vandermonde.py
      newton_interpolation.py
      lagrange.py
      spline.py
      spline_cubic.py
      compare.py
      common.py
  docs/                            Documentación por método (markdown)
frontend/
  index.html
  styles.css
  app.js
```

Documentación detallada de cada método en [`backend-python/docs/README.md`](backend-python/docs/README.md).

## Notas didácticas

- Algoritmos implementados a mano: no se usa `np.linalg.solve` ni `scipy.interpolate`. NumPy solo aparece para operaciones vectoriales básicas.
- Las derivadas se calculan simbólicamente con SymPy (`sp.diff`).
- Las expresiones del usuario se parsean con `sp.sympify`, así que aceptan funciones estándar: `sin`, `cos`, `exp`, `log`, `sqrt`, etc.

## Métodos implementados

### Ecuaciones de una variable
Bisección, regla falsa, punto fijo, Newton-Raphson, secante, Newton modificado para raíces múltiples.

### Sistemas lineales `Ax=b`
Jacobi, Gauss-Seidel, SOR.

### Interpolación
Vandermonde, diferencias divididas de Newton, Lagrange, spline lineal, spline cúbico natural.

## Endpoints

### Raíces
```
POST /api/single/bisection
POST /api/single/falsePosition
POST /api/single/fixedPoint
POST /api/single/newton
POST /api/single/secant
POST /api/single/modifiedNewtonMultiplicity
POST /api/single/compareSingle
```

### Sistemas lineales
```
POST /api/linear/jacobi
POST /api/linear/gaussSeidel
POST /api/linear/sor
POST /api/linear/compareLinear
```

### Interpolación
```
POST /api/interpolation/vandermonde
POST /api/interpolation/dividedDifferences
POST /api/interpolation/lagrange
POST /api/interpolation/linearSpline
POST /api/interpolation/cubicSpline
POST /api/interpolation/compareInterpolation
```

### Salud
```
GET /api/health
```
Devuelve `{ "ok": true, "project": "Numerical Methods Fullstack (Python)" }`.

## Ejemplo de petición

```bash
curl -X POST http://localhost:3000/api/single/newton \
  -H "Content-Type: application/json" \
  -d '{"fn":"x^3-x-2","x0":1.5,"tol":1e-6,"maxIter":50}'
```
