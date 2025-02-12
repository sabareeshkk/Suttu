from src.request.HttpRequest import HttpRequest
from src.response.HttpResponse import HttpResponse

def accept_connection(connection):
    """Accept an incoming connection, parse request, and send a response."""
    try:
        # Receive the incoming request data
        request = HttpRequest(connection)
        response = HttpResponse(connection)
        print(request, response, dir(request))
        # TODO: make decorator for routes
        # TODO: add timeouts
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
