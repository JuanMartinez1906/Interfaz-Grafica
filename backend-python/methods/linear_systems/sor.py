from .common import iterate


def sor(payload):
    omega = float(payload.get('omega', 1))
    if omega <= 0 or omega >= 2:
        raise ValueError('Para SOR, omega debe estar entre 0 y 2.')
    return iterate(payload, 'sor')
