# Spline cúbico natural

## Idea
Polinomio cúbico distinto en cada subintervalo [xᵢ, xᵢ₊₁], imponiendo continuidad de S, S' y S'' en los nodos interiores. La condición "natural" fija S''(x₀)=S''(xₙ)=0.

## Sistema a resolver
Sea hᵢ = xᵢ₊₁ - xᵢ y Mᵢ = S''(xᵢ). Para i=1..n-1:
```
hᵢ₋₁·Mᵢ₋₁ + 2(hᵢ₋₁+hᵢ)·Mᵢ + hᵢ·Mᵢ₊₁ = 6·((yᵢ₊₁-yᵢ)/hᵢ - (yᵢ-yᵢ₋₁)/hᵢ₋₁)
```
Con M₀ = Mₙ = 0 (spline natural). Sistema tridiagonal.

## Polinomio por segmento
```
Sᵢ(x) = Mᵢ(xᵢ₊₁-x)³/(6hᵢ) + Mᵢ₊₁(x-xᵢ)³/(6hᵢ)
       + (yᵢ - Mᵢhᵢ²/6)(xᵢ₊₁-x)/hᵢ
       + (yᵢ₊₁ - Mᵢ₊₁hᵢ²/6)(x-xᵢ)/hᵢ
```

## Ventajas
- Curva suave (C²) sin oscilaciones de Runge.
- Sistema lineal pequeño y tridiagonal.

## Implementación
[`methods/interpolation/spline_cubic.py`](../../methods/interpolation/spline_cubic.py)
