# Regla falsa (Regula Falsi)

## Idea
Como bisección, pero en vez de partir el intervalo a la mitad, se usa la intersección de la recta secante con el eje x. Suele converger más rápido en funciones bien comportadas.

## Condiciones
- f continua en [a,b].
- f(a)·f(b) < 0.

## Iteración
```
x = b - f(b)·(b-a) / (f(b)-f(a))
```
Si f(a)·f(x) < 0 → b = x; si no → a = x.

## Criterios de paro
- |f(x)| < tol
- |xₖ - xₖ₋₁| < tol
- k > maxIter

## Convergencia
Superior a lineal en la mayoría de casos, pero puede estancarse cuando un extremo del intervalo no se actualiza (extremo "fijo").

## Implementación
[`methods/single_variable/false_position.py`](../../methods/single_variable/false_position.py)
