# Newton-Raphson

## Idea
Aproximar f por su recta tangente en xₖ y tomar como siguiente iterado el cruce de esa tangente con el eje x.

## Condiciones
- f y f' continuas cerca de la raíz.
- f'(xₖ) ≠ 0 durante todas las iteraciones.
- x₀ suficientemente cerca de la raíz.

## Iteración
```
x_{k+1} = x_k - f(x_k) / f'(x_k)
```

## Criterios de paro
- |f(xₖ)| < tol
- |xₖ₊₁ - xₖ| < tol
- k > maxIter

## Convergencia
Cuadrática para raíces simples (el número de cifras correctas se duplica en cada iteración). Solo lineal en raíces múltiples (ver Newton modificado).

## Implementación
La derivada se calcula simbólicamente con SymPy.
[`methods/single_variable/newton_raphson.py`](../../methods/single_variable/newton_raphson.py)
