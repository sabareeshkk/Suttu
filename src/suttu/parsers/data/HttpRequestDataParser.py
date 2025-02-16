from abc import ABC, abstractmethod

from src.suttu.common import constants


class HttpRequestDataParser(ABC):
    """
    Abstract class for extracting HTTP request data based on
    Content-Length or Transfer-Encoding.
    """
    def __init__(self, connection, headers, data):
        """
        Initialize with a connection object (e.g., a socket).
        :param connection: The connection object to read data from.
        """
        self.connection = connection
        self.headers = headers
        self.data = data

    @abstractmethod
    def parse(self):
        """
        Abstract method to extract data from the request.
        This must be implemented by subclasses.
        """
        pass

    def parse_data(self):
        # get header and body
        body = self.data.split(constants.REQ_HEADER_SEPERATOR)[1]
        return body