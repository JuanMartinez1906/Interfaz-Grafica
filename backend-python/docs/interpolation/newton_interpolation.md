# Diferencias divididas de Newton

## Idea
Construir el polinomio interpolante en forma de Newton:
```
P(x) = a₀ + a₁(x-x₀) + a₂(x-x₀)(x-x₁) + ... + aₙ(x-x₀)...(x-xₙ₋₁)
```
donde aᵢ = f[x₀,...,xᵢ] son diferencias divididas.

## Diferencias divididas (recurrencia)
```
f[xᵢ] = yᵢ
f[xᵢ,...,xᵢ₊ⱼ] = ( f[xᵢ₊₁,...,xᵢ₊ⱼ] - f[xᵢ,...,xᵢ₊ⱼ₋₁] ) / (xᵢ₊ⱼ - xᵢ)
```

## Ventajas
- Agregar un punto nuevo solo cuesta una columna adicional (no rehacer todo).
- Numéricamente más estable que Vandermonde.

## Implementación
[`methods/interpolation/newton_interpolation.py`](../../methods/interpolation/newton_interpolation.py)
