import functools


class EndpointRegister(type):
    """Registers an enpoint to the class endpoints list."""
    def __init__(cls, name, bases, attrs):
        super(EndpointRegister, cls).__init__(name, bases, attrs)
        cls.endpoints = []
        for key, val in attrs.items():
            end_point = getattr(val, '_endpoint', None)
            if end_point is not None and end_point not in cls.endpoints:
                cls.endpoints.append(end_point)


def endpoint(end_point: str):
    """A class function decorator for endpoints. Passes the endpoint to the function as a kwarg."""
    def decorator(func):
        func = functools.partialmethod(func, endpoint=end_point)
        func._endpoint = end_point
        return func
    return decorator
