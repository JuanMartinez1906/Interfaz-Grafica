# Gauss-Seidel

## Idea
Como Jacobi, pero al actualizar xᵢ se usan los valores **ya actualizados** xⱼ del mismo paso para j<i. Suele converger más rápido que Jacobi.

## Condiciones (suficientes)
- A diagonal estrictamente dominante, o
- A simétrica definida positiva.

## Iteración
Para i = 1..n:
```
x_i^{(k+1)} = ( b_i - Σ_{j<i} a_ij · x_j^{(k+1)} - Σ_{j>i} a_ij · x_j^{(k)} ) / a_ii
```

## Criterios de paro
- ‖x^{(k+1)} - x^{(k)}‖∞ < tol
- k > maxIter

## Implementación
[`methods/linear_systems/gauss_seidel.py`](../../methods/linear_systems/gauss_seidel.py)
