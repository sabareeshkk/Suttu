from ..common import REQ_HEADER_SEPERATOR, HTTP_CONTENT_LENGTH, HTTP_TRANSFER_ENCODING
from ..parsers import ContentLengthParser, RequestHeaderParser, TransferEncodingParser

class HttpRequest:
    """
    this will create a http request object
    """

    def __init__(self, connection, buffer_size=16):
        self.connection = connection
        self.buffer_size = buffer_size
        self.headers = None
        self.data = b""
        self.body = b""
        self.__run()


    def __run(self):
        """
        entry point
        :return:
        """
        self.__receive_data()
        self.__parse_request_headers()
        self.__parse_request_data()

    def __receive_data(self):
        """
        initial data receiver and parsing header upto\r\n\r\n
        Receives data from the connection until the header separator is found.
        """
        while True:
            try:
                buffer = self.connection.recv(self.buffer_size)
                if not buffer:
                    break
                self.data += buffer
                if REQ_HEADER_SEPERATOR in self.data:
                    break
            except Exception as e:
                print(f"Error receiving data: {e}")
                raise  # Re-raise the exception to propagate it
        return self.data

    def __parse_request_headers(self):
        """
        parse the request header
        :return:
        """
        self.headers = RequestHeaderParser(self.data).headers

    def __parse_request_data(self):
        """Parse the request data depending on content type or transfer encoding."""
        try:
            if HTTP_CONTENT_LENGTH in self.headers:
                data = self.__parse_with_content_length().parse()
                self.body = data
            elif HTTP_TRANSFER_ENCODING in self.headers:
                data = self.__parse_with_transfer_encoding().parse()
                self.body = data
            return self.body
        except Exception as e:
            print(f"Error parsing request data: {e}")
            raise  # Re-raise the exception to propagate it

    def __parse_with_content_length(self):
        """Parse request data with content length."""
        try:
            return ContentLengthParser(self.connection, self.headers, self.data)
        except Exception as e:
            print(f"Error parsing content length: {e}")
            raise  # Re-raise the exception to propagate it

    def __parse_with_transfer_encoding(self):
        """Parse request data with transfer encoding."""
        try:
            return TransferEncodingParser(self.connection, self.headers, self.data)
        except Exception as e:
            print(f"Error parsing transfer encoding: {e}")
            raise  # Re-raise the exception to propagate it
