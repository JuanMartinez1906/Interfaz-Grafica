# Lagrange

## Idea
Expresar el polinomio interpolante como combinación de polinomios base Lᵢ que valen 1 en xᵢ y 0 en los demás nodos.

## Fórmula
```
P(x) = Σ yᵢ · Lᵢ(x)
Lᵢ(x) = Π_{j≠i} (x - xⱼ) / (xᵢ - xⱼ)
```

## Ventajas
- Forma simétrica y elegante; no requiere resolver sistemas.

## Desventajas
- Agregar un nuevo punto obliga a recalcular todos los Lᵢ.
- Inestabilidad numérica si los nodos están muy cerca.

## Implementación
[`methods/interpolation/lagrange.py`](../../methods/interpolation/lagrange.py)
