import socket
import threading

from .app import App
from .common import constants


class Suttu(App):
    """
    Initial entry point of the application
    """

    def __init__(self):
        # TODO:  make it accept __name__ for static and other files serving

        self.router_map = {}

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((constants.HOST, constants.PORT))
        sock.listen(5)
        print(f"server {constants.HOST} listening on port {constants.PORT}")

        while True:
            # Wait for a connection
            print("waiting for connection")
            connection, client_address = sock.accept()
            # Creating a thread with arguments
            thread = threading.Thread(target=self.accept_connection, args=(connection,))

            # Start the thread
            thread.start()

            # Wait for the thread to finish
            thread.join()




