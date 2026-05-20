# Secante

## Idea
Aproximar f'(xₖ) por la pendiente de la secante entre los dos últimos iterados. Evita evaluar derivadas analíticas.

## Condiciones
- f continua cerca de la raíz.
- x₀ y x₁ cercanos a la raíz.
- f(xₖ) ≠ f(xₖ₋₁).

## Iteración
```
x_{k+1} = x_k - f(x_k)·(x_k - x_{k-1}) / (f(x_k) - f(x_{k-1}))
```

## Criterios de paro
- |f(xₖ)| < tol
- |xₖ₊₁ - xₖ| < tol
- k > maxIter

## Convergencia
Orden φ ≈ 1.618 (superlinear, inferior a Newton pero sin necesidad de calcular f').

## Implementación
[`methods/single_variable/secant.py`](../../methods/single_variable/secant.py)
