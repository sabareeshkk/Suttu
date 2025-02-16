

class InvalidArgumentException(Exception):
    """Exception raised for invalid arguments."""
    def __init__(self, message="Argument cannot be None"):
        self.message = message
        super().__init__(self.message)
