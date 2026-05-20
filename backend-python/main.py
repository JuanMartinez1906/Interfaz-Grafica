from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from methods import single_variable as single
from methods import linear_systems as linear
from methods import interpolation as interp

app = FastAPI(title='Numerical Methods Fullstack (Python)')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

SINGLE_METHODS = {
    'bisection': single.bisection,
    'falsePosition': single.false_position,
    'fixedPoint': single.fixed_point,
    'newton': single.newton,
    'secant': single.secant,
    'modifiedNewtonMultiplicity': single.modified_newton_multiplicity,
    'compareSingle': single.compare_single,
}
LINEAR_METHODS = {
    'jacobi': linear.jacobi,
    'gaussSeidel': linear.gauss_seidel,
    'sor': linear.sor,
    'compareLinear': linear.compare_linear,
}
INTERP_METHODS = {
    'vandermonde': interp.vandermonde,
    'dividedDifferences': interp.divided_differences,
    'lagrange': interp.lagrange,
    'linearSpline': interp.linear_spline,
    'cubicSpline': interp.cubic_spline,
    'compareInterpolation': interp.compare_interpolation,
}


async def _run(registry, name, request: Request):
    fn = registry.get(name)
    if fn is None:
        return JSONResponse({'success': False, 'error': 'Método no encontrado'}, status_code=404)
    try:
        payload = await request.json()
        return fn(payload or {})
    except Exception as e:
        return JSONResponse({'success': False, 'error': str(e)}, status_code=400)


@app.post('/api/single/{name}')
async def single_route(name: str, request: Request):
    return await _run(SINGLE_METHODS, name, request)


@app.post('/api/linear/{name}')
async def linear_route(name: str, request: Request):
    return await _run(LINEAR_METHODS, name, request)


@app.post('/api/interpolation/{name}')
async def interp_route(name: str, request: Request):
    return await _run(INTERP_METHODS, name, request)


@app.get('/api/health')
def health():
    return {'ok': True, 'project': 'Numerical Methods Fullstack (Python)'}


FRONTEND_DIR = Path(__file__).resolve().parent.parent / 'frontend'
if FRONTEND_DIR.exists():
    app.mount('/', StaticFiles(directory=str(FRONTEND_DIR), html=True), name='frontend')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=3000)
