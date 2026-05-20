import math
import numpy as np
from utils import validate_linear, norm_inf


def ok(method, x, iterations, error, table):
    return {
        'method': method,
        'success': True,
        'x': x,
        'iterations': iterations,
        'error': error,
        'table': table,
    }


def label(mode, omega):
    if mode == 'jacobi':
        return 'Jacobi'
    if mode == 'sor':
        return f'SOR ω={omega}'
    return 'Gauss-Seidel'


def iterate(payload, mode):
    A = payload['A']
    b = payload['b']
    x0 = payload['x0']
    tol = float(payload.get('tol', 1e-7))
    max_iter = int(payload.get('maxIter', 100))
    omega = float(payload.get('omega', 1))
    validate_linear(A, b, x0)
    n = len(A)
    A_np = np.array(A, dtype=float)
    b_np = np.array(b, dtype=float)
    x = np.array(x0, dtype=float)
    table = []
    err = math.inf
    for k in range(1, max_iter + 1):
        prev = x.copy()
        nxt = x.copy()
        for i in range(n):
            if abs(A_np[i, i]) < 1e-14:
                raise ValueError('Hay un cero en la diagonal principal.')
            source = prev if mode == 'jacobi' else nxt
            s = A_np[i, :i] @ source[:i] + A_np[i, i + 1:] @ source[i + 1:]
            xi = (b_np[i] - s) / A_np[i, i]
            nxt[i] = (1 - omega) * prev[i] + omega * xi if mode == 'sor' else xi
        x = nxt
        err = norm_inf(x - prev)
        table.append({'k': k, 'x': x.tolist(), 'error': err})
        if err < tol:
            return ok(label(mode, omega), x.tolist(), k, err, table)
    return ok(label(mode, omega), x.tolist(), max_iter, err, table)
