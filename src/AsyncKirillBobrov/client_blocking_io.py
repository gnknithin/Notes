import socket
import sys
import time


def blocking_client() -> None:
    host = socket.gethostname()
    port = 12345
    # create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _sock:
        while True:
            _sock.connect((host, port))
            while True:
                data = str.encode(sys.argv[1])
                _ = _sock.send(data)
                time.sleep(0.5)
