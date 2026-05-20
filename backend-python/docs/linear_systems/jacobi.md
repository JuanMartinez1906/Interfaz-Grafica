# Jacobi

## Idea
Despejar xᵢ de la i-ésima ecuación usando los demás xⱼ del paso anterior. Cada componente se actualiza independientemente.

## Condiciones (suficientes)
- A diagonal estrictamente dominante por filas: |aᵢᵢ| > Σⱼ≠ᵢ |aᵢⱼ|.
- O ρ(M) < 1, donde M = D⁻¹(L+U).

## Iteración
Para i = 1..n:
```
x_i^{(k+1)} = ( b_i - Σ_{j≠i} a_ij · x_j^{(k)} ) / a_ii
```

## Criterios de paro
- ‖x^{(k+1)} - x^{(k)}‖∞ < tol
- k > maxIter

## Implementación
[`methods/linear_systems/jacobi.py`](../../methods/linear_systems/jacobi.py)
