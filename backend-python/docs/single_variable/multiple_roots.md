# Newton modificado para raíces múltiples

## Idea
Cuando la raíz tiene multiplicidad m, Newton estándar pierde convergencia cuadrática. Se corrige multiplicando el paso por m.

## Condiciones
- Se conoce (o se estima) la multiplicidad m de la raíz.
- f' continua y no nula en las iteraciones.

## Iteración
```
x_{k+1} = x_k - m · f(x_k) / f'(x_k)
```

## Criterios de paro
- |f(xₖ)| < tol
- |xₖ₊₁ - xₖ| < tol
- k > maxIter

## Convergencia
Cuadrática siempre que m sea la multiplicidad correcta de la raíz.

## Implementación
[`methods/single_variable/multiple_roots.py`](../../methods/single_variable/multiple_roots.py)
