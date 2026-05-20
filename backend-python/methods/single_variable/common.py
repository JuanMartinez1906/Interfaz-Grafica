def ok(method, root, iterations, error, table):
    return {
        'method': method,
        'success': True,
        'root': root,
        'iterations': iterations,
        'error': error,
        'table': table,
    }


def guard(max_iter):
    if max_iter > 1000:
        raise ValueError('maxIter no puede superar 1000.')
