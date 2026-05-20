import math
from utils import compile_function
from .common import ok, guard


def bisection(payload):
    fn = payload['fn']
    a = float(payload['a'])
    b = float(payload['b'])
    tol = float(payload.get('tol', 1e-7))
    max_iter = int(payload.get('maxIter', 100))
    guard(max_iter)
    f = compile_function(fn)
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError('Bisección requiere cambio de signo: f(a)f(b)<0.')
    table = []
    mid = a
    err = math.inf
    for k in range(1, max_iter + 1):
        prev = mid
        mid = (a + b) / 2
        fm = f(mid)
        err = abs(b - a) if k == 1 else abs(mid - prev)
        table.append({'k': k, 'a': a, 'b': b, 'x': mid, 'fx': fm, 'error': err})
        if abs(fm) < tol or err < tol:
            return ok('Bisección', mid, k, err, table)
        if fa * fm < 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm
    return ok('Bisección', mid, max_iter, err, table)
