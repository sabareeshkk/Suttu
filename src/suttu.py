import socket
from src.parsers import helper
from src.parsers.data.ContentLengthDataParser import HttpContentLengthParser
from src.parsers.data.TransferEncodingDataParser import TransferEncodingParser
from src.common import constants

sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((constants.HOST, constants.PORT))
sock.listen(5)
print(f"server {constants.HOST} listening on port {constants.PORT}")


while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    print("waiting for connection")

    try:
        data = bytearray()
        while True:
            buffer = connection.recv(10)
            if not buffer:
                break
            data += buffer
            if constants.REQ_HEADER_SEPERATOR in data:
                req_headers = helper.parse_headers(data)
                # TODO: parse path and query params
                req_data =  helper.parse_data(data)
                if constants.HTTP_CONTENT_LENGTH in req_headers:
                    parser = HttpContentLengthParser(connection, req_headers)
                    req_data = parser.parse(req_data)
                elif constants.HTTP_TRANSFER_ENCODING in req_headers:
                    parser = TransferEncodingParser(connection, req_headers)
                    req_data = parser.parse(req_data)
                break
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: 13\r\n"
            "\r\n"
            "Hello, world!"
        )
        connection.sendall(response.encode())
    finally:
        connection.close()


