# Vandermonde

## Idea
Buscar el polinomio P(x)=a₀+a₁x+...+aₙxⁿ que pase por n+1 puntos resolviendo el sistema lineal Vc = y, donde V es la matriz de Vandermonde Vᵢⱼ = xᵢʲ.

## Condiciones
- Los xᵢ deben ser distintos (si no, V es singular).

## Procedimiento
1. Construir V con Vᵢⱼ = xᵢʲ.
2. Resolver V·c = y (eliminación gaussiana).
3. Los coeficientes c son los del polinomio interpolante.

## Limitaciones
- V está mal condicionada cuando los xᵢ están cerca. Para n grande pierde precisión.
- Para uso práctico se prefieren diferencias divididas o Lagrange.

## Implementación
[`methods/interpolation/vandermonde.py`](../../methods/interpolation/vandermonde.py)
