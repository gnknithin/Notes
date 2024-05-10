import select
import socket
from typing import Any, List


def non_blocking_io_server() -> None:
    host = socket.gethostname()
    port = 12345
    # create TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _sock:
        _sock.setblocking(0)
        # bind the socket to the port
        _sock.bind((host, port))
        # liste for incoming connections
        _sock.listen(5)
        print("Server started...")
        # sockets from which we expect to read
        inputs = [_sock]
        outputs: List[Any] = []
        while inputs:
            # wait for at least one of the sockets to be ready for processing
            readable, writable, exceptional = select.select(
                inputs, outputs, inputs, None
            )
            for s in readable:
                if s is _sock:
                    # accept new connection
                    conn, addr = s.accept()
                    inputs.append(conn)
                else:
                    # receive data from the existing connection
                    data = s.recv(1024)
                    if data:
                        print(data)
                    else:
                        # close connection
                        inputs.remove(s)
                        s.close()
