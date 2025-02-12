import socket
import threading

from src.app.app import accept_connection
from src.common import constants

sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((constants.HOST, constants.PORT))
sock.listen(5)
print(f"server {constants.HOST} listening on port {constants.PORT}")

class Suttu:
    """
    Initial entry point of the application
    """
    def __init__(self):
        # TODO:  make it accept __name__ for static and other files serving
        self.run()

    def run(self):

        while True:
            # Wait for a connection
            print("waiting for connection")
            connection, client_address = sock.accept()
            # Creating a thread with arguments
            thread = threading.Thread(target=accept_connection, args=(connection,))

            # Start the thread
            thread.start()

            # Wait for the thread to finish
            thread.join()

if __name__ == "__main__":
    suttu = Suttu()



