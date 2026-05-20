import math
from utils import compile_function
from .common import ok, guard


def secant(payload):
    fn = payload['fn']
    x0 = float(payload['x0'])
    x1 = float(payload['x1'])
    tol = float(payload.get('tol', 1e-7))
    max_iter = int(payload.get('maxIter', 100))
    guard(max_iter)
    f = compile_function(fn)
    table = []
    xa, xb = x0, x1
    err = math.inf
    for k in range(1, max_iter + 1):
        f0 = f(xa)
        f1 = f(xb)
        if abs(f1 - f0) < 1e-14:
            raise ValueError('División por cero en secante.')
        x = xb - f1 * (xb - xa) / (f1 - f0)
        err = abs(x - xb)
        table.append({'k': k, 'x0': xa, 'x1': xb, 'x': x, 'fx': f(x), 'error': err})
        xa, xb = xb, x
        if abs(f(x)) < tol or err < tol:
            return ok('Secante', x, k, err, table)
    return ok('Secante', xb, max_iter, err, table)
