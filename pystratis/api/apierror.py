class APIError(Exception):
    """Represents an API error message response.

    Attributes:
        code (int): The API error code.
        message (str): The error message.
    """
    def __init__(self, code: int, message: str):
        """Initializes the exception."""
        self.code = code
        self.message = message
