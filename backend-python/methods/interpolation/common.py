def check_points(points):
    if not isinstance(points, list) or not (2 <= len(points) <= 8):
        raise ValueError('Debes enviar entre 2 y 8 puntos.')
    xs = [float(p['x']) for p in points]
    if len(set(xs)) != len(xs):
        raise ValueError('Los valores de x no pueden repetirse.')
    return sorted(
        [{'x': float(p['x']), 'y': float(p['y'])} for p in points],
        key=lambda p: p['x'],
    )


def eval_poly(coefs, x):
    return float(sum(c * x ** i for i, c in enumerate(coefs)))
