from .common import check_points


def linear_spline(payload):
    pts = check_points(payload['points'])
    eval_x = payload.get('evalX')
    segments = []
    for i in range(len(pts) - 1):
        m = (pts[i + 1]['y'] - pts[i]['y']) / (pts[i + 1]['x'] - pts[i]['x'])
        b = pts[i]['y'] - m * pts[i]['x']
        sign = '+' if b >= 0 else '-'
        segments.append({
            'from': pts[i]['x'],
            'to': pts[i + 1]['x'],
            'm': m,
            'b': b,
            'equation': f'S{i}(x)={m:.8g}x {sign} {abs(b):.8g}',
        })
    value = None
    if eval_x is not None:
        x = float(eval_x)
        seg = next((s for s in segments if s['from'] <= x <= s['to']), None)
        if seg is None:
            raise ValueError('evalX está fuera del rango de los puntos.')
        value = seg['m'] * x + seg['b']
    return {'method': 'Spline lineal', 'success': True, 'segments': segments, 'value': value}
