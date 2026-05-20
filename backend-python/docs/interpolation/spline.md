# Spline lineal

## Idea
Unir los puntos consecutivos con segmentos de recta. Es la interpolación a trozos más simple.

## Fórmula por segmento
Para xᵢ ≤ x ≤ xᵢ₊₁:
```
Sᵢ(x) = mᵢ · x + bᵢ
mᵢ = (yᵢ₊₁ - yᵢ) / (xᵢ₊₁ - xᵢ)
bᵢ = yᵢ - mᵢ · xᵢ
```

## Propiedades
- Continua en los nodos.
- Derivada **no** continua en general (no es suave).
- Sin oscilaciones tipo Runge (problema típico de polinomios de alto grado).

## Implementación
[`methods/interpolation/spline.py`](../../methods/interpolation/spline.py)
