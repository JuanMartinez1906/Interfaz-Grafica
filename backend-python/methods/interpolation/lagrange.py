from .common import check_points


def lagrange(payload):
    pts = check_points(payload['points'])
    eval_x = payload.get('evalX')
    terms = []
    for i, pi in enumerate(pts):
        denom = 1.0
        for j, pj in enumerate(pts):
            if i != j:
                denom *= pi['x'] - pj['x']
        terms.append({'i': i, 'yi': pi['y'], 'xi': pi['x'], 'denominator': denom})
    value = None
    if eval_x is not None:
        x = float(eval_x)
        value = 0.0
        for i, t in enumerate(terms):
            prod = 1.0
            for j, pj in enumerate(pts):
                if i != j:
                    prod *= x - pj['x']
            value += t['yi'] * prod / t['denominator']
    return {
        'method': 'Lagrange',
        'success': True,
        'terms': terms,
        'value': value,
        'form': 'P(x)=Σ yi Li(x), donde Li(x)=Π(x-xj)/(xi-xj)',
    }
