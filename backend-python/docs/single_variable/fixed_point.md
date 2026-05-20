# Punto fijo

## Idea
Reescribir f(x)=0 como x = g(x). La sucesión xₖ₊₁ = g(xₖ) converge al punto fijo si g es contractiva en un entorno de la raíz.

## Condiciones
- |g'(x)| < 1 en un entorno de la raíz (condición suficiente de convergencia).
- x₀ suficientemente cercano a la raíz.

## Iteración
```
x_{k+1} = g(x_k)
```

## Criterios de paro
- |xₖ₊₁ - xₖ| < tol
- k > maxIter

## Convergencia
Lineal cuando |g'(r)| ≠ 0. Si g'(r)=0, la convergencia es al menos cuadrática.

## Implementación
[`methods/single_variable/fixed_point.py`](../../methods/single_variable/fixed_point.py)
