from src.suttu.parsers.data.HttpRequestDataParser import HttpRequestDataParser
from src.suttu.common import HTTP_CONTENT_LENGTH

class HttpContentLengthParser(HttpRequestDataParser):
    """
    parse http request data based on the content-length header
    """

    def parse(self):
        """
        Extract the body data based on the Content-Length header.
        :return: The extracted data as bytes.
        """
        content_length = int(self.headers.get(HTTP_CONTENT_LENGTH, 0))
        if content_length <= 0:
            raise ValueError("Invalid or missing Content-Length header.")

        body = self.parse_data()
        while len(body) < content_length:
            chunk = self.connection.recv(min(content_length - len(body), 1024))
            if not chunk:
                raise ConnectionError("Connection closed before all data was received.")
            body += chunk

        return body
