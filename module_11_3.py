def introspection_info(obj):
    import inspect

    info = {
        'type': type(obj).__name__,
        'attributes': [],
        'methods': [],
        'module': inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'builtins' if isinstance(obj, (
        int, str, float)) else None,
    }

    if hasattr(obj, '__dict__'):
        info['attributes'] = list(obj.__dict__.keys())

    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    if not info['attributes']:
        info['attributes'] = ['None']

    return info


number_info = introspection_info(42)
print(number_info)
