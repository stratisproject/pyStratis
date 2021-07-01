import functools
import os


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
        # Returns the original function when using sphinx.
        sphinx_build = bool(os.environ.get('SPHINX_BUILD', ''))
        if sphinx_build:
            return func

        partial_func = functools.partialmethod(func, endpoint=end_point)
        functools.update_wrapper(partial_func, func)
        partial_func._endpoint = end_point
        return partial_func
    return decorator
