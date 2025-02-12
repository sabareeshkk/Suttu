class HttpResponse:
    """
    this will create a http response object
    """

    def __init__(self, connection):
        self.connection = connection

    # TODO: move to base class may be later
    def close(self):
        self.connection.close()

    #  send response
    def json(self, data):
        """
        send http response in json format
        :param data:
        :return: None
        """
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: application/json\r\n"
            f"Content-Length: {len(data)}\r\n"
            "\r\n"
            f"{data}"
        )
        self.connection.sendall(response.encode())

    def send(self, data):
        """Send a simple HTTP response."""
        try:
            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(data)}\r\n"
                "\r\n"
                f"{data}"
            )
            self.connection.sendall(response.encode())
        except Exception as e:
            print(f"Error sending response: {e}")
            raise  # Re-raise the exception to propagate it



