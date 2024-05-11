import socket
import threading


def handler(client: socket.socket) -> None:
    while True:
        data = client.recv(1024)
        if data:
            print(data)


def threads() -> None:
    host = socket.gethostname()
    port = 12345
    # create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _sock:
        # bind the socket to the port
        _sock.bind((host, port))
        # listen for incoming connections
        _sock.listen(5)
        print("Server started...")
        while True:
            client, addr = _sock.accept()
            threading.Thread(target=handler, args=(client,)).start()
