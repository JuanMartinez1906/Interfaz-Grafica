from .bisection import bisection
from .false_position import false_position
from .newton_raphson import newton
from .secant import secant


def compare_single(payload):
    out = []

    def try_run(name, fn):
        try:
            out.append(fn(payload))
        except Exception as e:
            out.append({'method': name, 'success': False, 'errorMessage': str(e)})

    try_run('Bisección', bisection)
    try_run('Regla falsa', false_position)
    if 'x0' in payload:
        try_run('Newton-Raphson', newton)
    if 'x0' in payload and 'x1' in payload:
        try_run('Secante', secant)
    out.sort(key=lambda r: (0 if r.get('success') else 1, r.get('iterations', 9999)))
    return out
