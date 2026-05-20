from .jacobi import jacobi
from .gauss_seidel import gauss_seidel
from .sor import sor


def compare_linear(payload):
    runs = []

    def call(name, fn, p=None):
        try:
            runs.append(fn(p if p is not None else payload))
        except Exception as e:
            runs.append({'method': name, 'success': False, 'errorMessage': str(e)})

    call('Jacobi', jacobi)
    call('Gauss-Seidel', gauss_seidel)
    for w in (0.8, 1.0, 1.2):
        call(f'SOR ω={w}', sor, {**payload, 'omega': w})
    runs.sort(key=lambda r: (0 if r.get('success') else 1, r.get('iterations', 9999)))
    return runs
