import math
from utils import compile_function
from .common import ok, guard


def fixed_point(payload):
    g = payload['g']
    x0 = float(payload['x0'])
    tol = float(payload.get('tol', 1e-7))
    max_iter = int(payload.get('maxIter', 100))
    guard(max_iter)
    gx = compile_function(g)
    table = []
    x = x0
    err = math.inf
    for k in range(1, max_iter + 1):
        xn = gx(x)
        err = abs(xn - x)
        table.append({'k': k, 'x': xn, 'gx': xn, 'error': err})
        x = xn
        if err < tol:
            return ok('Punto fijo', x, k, err, table)
    return ok('Punto fijo', x, max_iter, err, table)
