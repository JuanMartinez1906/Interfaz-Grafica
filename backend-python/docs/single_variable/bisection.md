# Bisección

## Idea
Si f es continua en [a,b] y f(a)·f(b) < 0, por el Teorema del Valor Intermedio existe al menos una raíz en (a,b). Se divide el intervalo a la mitad y se conserva el sub-intervalo donde sigue habiendo cambio de signo.

## Condiciones
- f continua en [a,b].
- f(a)·f(b) < 0.

## Iteración
1. m = (a+b)/2
2. Si f(a)·f(m) < 0 → b = m; si no → a = m.
3. Repetir hasta |f(m)| < tol o |b-a| < tol.

## Criterios de paro
- |f(m)| < tol
- |xₖ - xₖ₋₁| < tol
- k > maxIter

## Convergencia
Lineal. El error se divide por 2 en cada iteración: |b-a|/2ᵏ.

## Implementación
[`methods/single_variable/bisection.py`](../../methods/single_variable/bisection.py)
