from src.parsers.data.HttpDataParser import HttpDataParser

class TransferEncodingParser(HttpDataParser):
    """
    parse request data based on transfer encoding (chunked)
    # TODO: other formats also supported like compress, deflate, gzip
    """
    def parse(self, data):
        """
        Extract the body data using chunked transfer encoding.
        :return: The extracted data as bytes.
        """
        extracted_data = b""
        while True:

            while data.find(b"\r\n") < 0:
                data += self.connection.recv(16)

            chunk_len_pos = data.find(b"\r\n")
            chunk_size = int(data[:chunk_len_pos], 16)

            if chunk_size == 0:  # End of chunks
                break

            chunk_data_start_pos = chunk_len_pos + 2
            chunk_data_end_pos = chunk_data_start_pos + chunk_size
            # initialize chunk data
            chunk_data = data[chunk_data_start_pos: chunk_data_end_pos]

            if len(chunk_data) < chunk_size:
                # read chuk data
                while len(chunk_data) < chunk_size:
                    chunk = self.connection.recv(min(chunk_size - len(chunk_data), 1024))
                    if not chunk:
                        raise ConnectionError("Connection closed before all chunk data was received.")
                    chunk_data += chunk
                # Consume the trailing \r\n after the chunk
                self.connection.recv(2)
                data = b""
            else:
                if len(data[chunk_data_end_pos:]) >= 2:
                    data = data[chunk_data_end_pos + 2:]
                else:
                    self.connection.recv(2 - len(data[chunk_data_end_pos:]))
                    data = b""
            extracted_data += chunk_data
        return extracted_data
