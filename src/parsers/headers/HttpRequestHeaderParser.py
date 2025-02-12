# helper functions
from src.common import constants


class HttpRequestHeaderParser:
    def __init__(self, data):
        self.headers = self.parse(data)

    def parse(self, data):
        """Main method to parse the data."""
        headers, body = self.__split_data(data)
        header_arr = self.split_headers(headers)
        metadata = self.parse_req_header_meta(header_arr[0])
        header_data = self.parse_req_header_values(header_arr[1:])
        return {**metadata, **header_data}

    def __split_data(self, data):
        """Splits the incoming data into headers and body."""
        headers, body = data.split(constants.REQ_HEADER_SEPERATOR)
        return headers, body

    def split_headers(self, headers):
        """Splits headers into a list of header lines."""
        return headers.split(constants.HEADER_SEPERATOR)

    def parse_req_header_meta(self, http_req_metadata):
        """Parses the request line (method, path, and HTTP version)."""
        method, path, http_version = http_req_metadata.decode().strip().split(" ")
        http_version = http_version.split("/")[1]  # Extract version from HTTP/1.1
        return {"method": method, "path": path, "http_version": http_version}

    def parse_req_header_values(self, http_req_header_values):
        """Parses the headers into key-value pairs."""
        header_values = {}
        for req_buffer in http_req_header_values:
            head_key, head_value = req_buffer.decode().strip().split(": ")
            # TODO: Parse values according to their types (like int, bool, etc.)
            header_values[head_key] = head_value
        return header_values
