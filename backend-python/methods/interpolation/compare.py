from .vandermonde import vandermonde
from .newton_interpolation import divided_differences
from .lagrange import lagrange
from .spline import linear_spline
from .spline_cubic import cubic_spline


def compare_interpolation(payload):
    out = []
    for fn, name in [
        (vandermonde, 'vandermonde'),
        (divided_differences, 'dividedDifferences'),
        (lagrange, 'lagrange'),
        (linear_spline, 'linearSpline'),
        (cubic_spline, 'cubicSpline'),
    ]:
        try:
            out.append(fn(payload))
        except Exception as e:
            out.append({'method': name, 'success': False, 'errorMessage': str(e)})
    return out
