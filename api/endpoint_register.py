import functools


class EndpointRegister(type):
    """Registers an enpoint to the class endpoints list."""
    def __init__(cls, name, bases, attrs):
        super(EndpointRegister, cls).__init__(name, bases, attrs)
        cls.endpoints = []
        for key, val in attrs.items():
            endpoint = getattr(val, '_endpoint', None)
            if endpoint is not None and endpoint not in cls.endpoints:
                cls.endpoints.append(endpoint)


def endpoint(endpoint: str):
    """A class function decorator for endpoints. Passes the endpoint to the function as a kwarg."""
    def decorator(func):
        func = functools.partialmethod(func, endpoint=endpoint)
        func._endpoint = endpoint
        return func
    return decorator
