import math
from utils import compile_function
from .common import ok, guard


def false_position(payload):
    fn = payload['fn']
    a = float(payload['a'])
    b = float(payload['b'])
    tol = float(payload.get('tol', 1e-7))
    max_iter = int(payload.get('maxIter', 100))
    guard(max_iter)
    f = compile_function(fn)
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError('Regla falsa requiere cambio de signo: f(a)f(b)<0.')
    table = []
    x = a
    err = math.inf
    for k in range(1, max_iter + 1):
        prev = x
        x = b - fb * (b - a) / (fb - fa)
        fx = f(x)
        err = abs(x) if k == 1 else abs(x - prev)
        table.append({'k': k, 'a': a, 'b': b, 'x': x, 'fx': fx, 'error': err})
        if abs(fx) < tol or err < tol:
            return ok('Regla falsa', x, k, err, table)
        if fa * fx < 0:
            b, fb = x, fx
        else:
            a, fa = x, fx
    return ok('Regla falsa', x, max_iter, err, table)
