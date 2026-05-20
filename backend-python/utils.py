import math
import numpy as np
import sympy as sp

_x = sp.Symbol('x')


def _safe_lambdify(expr_sym):
    f = sp.lambdify(_x, expr_sym, modules=['numpy', 'math'])

    def wrapped(x):
        y = f(float(x))
        y = complex(y) if isinstance(y, complex) else y
        if isinstance(y, complex):
            if abs(y.imag) > 1e-12:
                raise ValueError('La función produjo un número complejo.')
            y = y.real
        y = float(y)
        if not math.isfinite(y):
            raise ValueError('La función no está definida o no es continua en ese punto.')
        return y

    return wrapped


def compile_function(expr):
    try:
        sym = sp.sympify(expr, locals={'e': sp.E, 'pi': sp.pi})
    except (sp.SympifyError, SyntaxError) as exc:
        raise ValueError(f'Expresión inválida: {exc}')
    return _safe_lambdify(sym)


def derivative_function(expr, order=1):
    sym = sp.sympify(expr, locals={'e': sp.E, 'pi': sp.pi})
    for _ in range(order):
        sym = sp.diff(sym, _x)
    return _safe_lambdify(sym)


def norm_inf(v):
    return float(np.max(np.abs(np.asarray(v, dtype=float))))


def validate_linear(A, b, x0):
    if not (isinstance(A, list) and isinstance(b, list) and isinstance(x0, list)):
        raise ValueError('A, b y x0 deben ser arreglos.')
    n = len(A)
    if n < 2 or n > 7:
        raise ValueError('El sistema debe tener tamaño entre 2 y 7.')
    if len(b) != n or len(x0) != n:
        raise ValueError('b y x0 deben tener el mismo tamaño que A.')
    for row in A:
        if not isinstance(row, list) or len(row) != n:
            raise ValueError('A debe ser cuadrada.')


def solve_linear_system(A, b):
    A = np.array(A, dtype=float).copy()
    b = np.array(b, dtype=float).copy()
    n = len(A)
    for k in range(n):
        piv = k + int(np.argmax(np.abs(A[k:, k])))
        if abs(A[piv, k]) < 1e-14:
            raise ValueError('La matriz es singular o casi singular.')
        if piv != k:
            A[[k, piv]] = A[[piv, k]]
            b[[k, piv]] = b[[piv, k]]
        for i in range(k + 1, n):
            f = A[i, k] / A[k, k]
            A[i, k:] -= f * A[k, k:]
            b[i] -= f * b[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - A[i, i + 1:] @ x[i + 1:]) / A[i, i]
    return x.tolist()


def poly_string(coefs):
    parts = []
    for i, c in enumerate(coefs):
        v = float(c)
        if abs(v) < 1e-12:
            continue
        if i == 0:
            parts.append(f'{v:.8g}')
        elif i == 1:
            parts.append(f'{v:.8g}x')
        else:
            parts.append(f'{v:.8g}x^{i}')
    if not parts:
        return '0'
    s = ' + '.join(reversed(parts))
    return s.replace('+ -', '- ')
