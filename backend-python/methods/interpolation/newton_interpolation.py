from .common import check_points


def divided_differences(payload):
    pts = check_points(payload['points'])
    eval_x = payload.get('evalX')
    n = len(pts)
    table = [[None] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = pts[i]['y']
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (pts[i + j]['x'] - pts[i]['x'])
    coeffs = [table[0][j] for j in range(n)]
    value = None
    if eval_x is not None:
        x = float(eval_x)
        value = 0.0
        for i, c in enumerate(coeffs):
            prod = 1.0
            for k in range(i):
                prod *= x - pts[k]['x']
            value += c * prod
    return {
        'method': 'Diferencias divididas de Newton',
        'success': True,
        'coefficients': coeffs,
        'table': table,
        'value': value,
        'form': 'P(x)=a0+a1(x-x0)+a2(x-x0)(x-x1)+...',
    }
