class APIError(Exception):
    """APIError handler."""
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
