from utils import solve_linear_system, poly_string
from .common import check_points, eval_poly


def vandermonde(payload):
    pts = check_points(payload['points'])
    eval_x = payload.get('evalX')
    n = len(pts)
    A = [[p['x'] ** j for j in range(n)] for p in pts]
    b = [p['y'] for p in pts]
    coefs = solve_linear_system(A, b)
    return {
        'method': 'Vandermonde',
        'success': True,
        'coefficients': coefs,
        'polynomial': poly_string(coefs),
        'value': eval_poly(coefs, float(eval_x)) if eval_x is not None else None,
    }
