import math
from utils import compile_function, derivative_function
from .common import ok, guard


def newton(payload):
    fn = payload['fn']
    x0 = float(payload['x0'])
    tol = float(payload.get('tol', 1e-7))
    max_iter = int(payload.get('maxIter', 100))
    guard(max_iter)
    f = compile_function(fn)
    df = derivative_function(fn, 1)
    table = []
    x = x0
    err = math.inf
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-14:
            raise ValueError('Derivada cercana a cero; Newton se detiene.')
        xn = x - fx / dfx
        err = abs(xn - x)
        table.append({'k': k, 'x': xn, 'fx': f(xn), 'dfx': dfx, 'error': err})
        x = xn
        if abs(f(x)) < tol or err < tol:
            return ok('Newton-Raphson', x, k, err, table)
    return ok('Newton-Raphson', x, max_iter, err, table)
