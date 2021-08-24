def main():
    import socket, threading, atexit

    def handle_exit():
        print("Stopping program")
        s.close()

    atexit.register(handle_exit)

    # Set up socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = "192.168.1.35"
    port = 12345

    s.bind((host, port))
    s.listen(5)
    print("Socket is listening")

    # Recieve messages from clients
    def recieve(name):
        global connections
        while 1:
            try:
                data = "<{0}>: {1}".format(name, (connections[name].recv(512).decode()))
            except:
                # Client disconnects
                print("Connection with {0} closed".format(name))
                del connections[name]
                data = "<{0}> has left the chat".format(name)
                [connections[a].sendall(data.encode()) for a in connections]
                break
            [connections[a].sendall(data.encode()) for a in connections]

    # Check for new clients attempting to connect
    global connections
    connections = {}
    while 1:
        conn, addr = s.accept()
        connections[(name := conn.recv(128).decode())] = conn
        print(name)
        (threading.Thread(target=recieve, args=[name])).start()
        [a.sendall(("<{0} has joined the chat>".format(name).encode())) for a in list(connections.values())]
        print("Connection established")


if __name__ == '__main__':
    main()
