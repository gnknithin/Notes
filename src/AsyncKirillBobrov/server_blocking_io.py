import socket


def blocking_server() -> None:
    host = socket.gethostname()
    port = 12345
    # create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as _sock:
        # bind the socket to the port
        _sock.bind((host, port))
        # listen for incoming connections
        _sock.listen(5)
        print("Server listening...")
        while True:
            # accepting the incoming connections, blocking
            conn, addr = _sock.accept()
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)  # receiving data, blocking
                if not data:
                    break
                print(data)
