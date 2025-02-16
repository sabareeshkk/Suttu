from abc import ABC

from src.suttu.request.HttpRequest import HttpRequest
from src.suttu.response.HttpResponse import HttpResponse

from src.suttu.Exceptions.InvalidArgumentException import InvalidArgumentException


class App(ABC):

    def accept_connection(self, connection):
        """Accept an incoming connection, parse request, and send a response."""
        try:
            # Receive the incoming request data
            request = HttpRequest(connection)
            response = HttpResponse(connection)
            print(request, response, dir(request))
            # FIXME: make context local for request object to set in thread
            # Send the HTTP response
            response.send(request.body.decode())

        except Exception as e:
            print(f"Error handling connection: {e}")
            # Handle any other exceptions that occurred during processing.
            # You could choose to send a 500 error or handle it in another way.
            try:
                connection.sendall("HTTP/1.1 500 Internal Server Error\r\n\r\n".encode())
            except Exception as send_error:
                print(f"Error sending error response: {send_error}")
        finally:
            try:
                connection.close()
            except Exception as close_error:
                print(f"Error closing connection: {close_error}")

    def route(self, path, methods=None):
        if path is None:
            raise InvalidArgumentException
        # TODO: make decorator for routes
        if methods is None:
            methods = ["GET", "POST", "PUT", "DELETE"]