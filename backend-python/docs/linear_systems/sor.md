# SOR (Successive Over-Relaxation)

## Idea
Combina el iterado de Gauss-Seidel con el valor anterior mediante un parámetro ω. Con ω óptimo puede acelerar significativamente la convergencia.

## Condiciones
- 0 < ω < 2 (Teorema de Kahan: necesaria para convergencia).
- A simétrica definida positiva ⇒ converge para todo ω ∈ (0,2).

## Iteración
Sea ẋᵢ el iterado de Gauss-Seidel:
```
x_i^{(k+1)} = (1-ω) · x_i^{(k)} + ω · ẋ_i
```
- ω = 1 → Gauss-Seidel.
- ω > 1 → sobre-relajación.
- ω < 1 → sub-relajación.

## Criterios de paro
- ‖x^{(k+1)} - x^{(k)}‖∞ < tol
- k > maxIter

## Implementación
[`methods/linear_systems/sor.py`](../../methods/linear_systems/sor.py)
