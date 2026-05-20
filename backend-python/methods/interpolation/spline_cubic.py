from utils import solve_linear_system
from .common import check_points


def cubic_spline(payload):
    pts = check_points(payload['points'])
    eval_x = payload.get('evalX')
    n = len(pts)
    h = [pts[i + 1]['x'] - pts[i]['x'] for i in range(n - 1)]
    A = [[0.0] * n for _ in range(n)]
    rhs = [0.0] * n
    A[0][0] = 1.0
    A[n - 1][n - 1] = 1.0
    for i in range(1, n - 1):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        rhs[i] = 6 * ((pts[i + 1]['y'] - pts[i]['y']) / h[i] - (pts[i]['y'] - pts[i - 1]['y']) / h[i - 1])
    M = solve_linear_system(A, rhs)
    segments = []
    for i in range(n - 1):
        segments.append({
            'from': pts[i]['x'],
            'to': pts[i + 1]['x'],
            'Mi': M[i],
            'Mi1': M[i + 1],
            'formula': 'Si(x)=Mi(xi+1-x)^3/(6h)+Mi+1(x-xi)^3/(6h)+(yi-Mi h^2/6)(xi+1-x)/h+(yi+1-Mi+1 h^2/6)(x-xi)/h',
        })

    def eval_seg(i, x):
        hi = h[i]
        xi, xi1 = pts[i]['x'], pts[i + 1]['x']
        yi, yi1 = pts[i]['y'], pts[i + 1]['y']
        return (
            M[i] * (xi1 - x) ** 3 / (6 * hi)
            + M[i + 1] * (x - xi) ** 3 / (6 * hi)
            + (yi - M[i] * hi * hi / 6) * (xi1 - x) / hi
            + (yi1 - M[i + 1] * hi * hi / 6) * (x - xi) / hi
        )

    value = None
    if eval_x is not None:
        x = float(eval_x)
        idx = next((i for i, s in enumerate(segments) if s['from'] <= x <= s['to']), -1)
        if idx < 0:
            raise ValueError('evalX está fuera del rango de los puntos.')
        value = eval_seg(idx, x)
    return {'method': 'Spline cúbico natural', 'success': True, 'M': M, 'segments': segments, 'value': value}
