from abc import ABC, abstractmethod

class HttpDataParser(ABC):
    """
    Abstract class for extracting HTTP request data based on
    Content-Length or Transfer-Encoding.
    """
    def __init__(self, connection, headers):
        """
        Initialize with a connection object (e.g., a socket).
        :param connection: The connection object to read data from.
        """
        self.connection = connection
        self.headers = headers

    @abstractmethod
    def parse(self, initial_data):
        """
        Abstract method to extract data from the request.
        This must be implemented by subclasses.
        """
        pass