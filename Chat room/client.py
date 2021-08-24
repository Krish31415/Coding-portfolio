def main():
    import socket, threading, atexit
    from tkinter import Tk, Entry, BOTTOM, END, Label, CENTER

    # Set up tkinter window
    root = Tk()
    root.title("Client")
    root.geometry("200x300")

    # Close socket when code stops
    def handle_exit():
        print("Stopping program")
        try:
            s.close()
        except:
            pass

    atexit.register(handle_exit)

    # Connect to server
    def connect(key):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = '192.168.1.35'
        port = 12345

        s.connect((host, port))
        print("Connection established")
        s.sendall(name.get().encode())
        threading.Thread(target=recieve).start()

        # change tkinter window
        name.pack_forget()
        root.configure(bg="black")

        (inputs := Entry(root, width=30)).pack(side=BOTTOM)

        # Send text
        def send(key):
            s.sendall((inputs.get()).encode())
            inputs.delete(0, END)

        inputs.bind("<Return>", send)

    # Recieve texts from server
    def recieve():
        while 1:
            try:
                data = s.recv(1024).decode()
                (Label(root, text=data, bg='black', fg='white')).pack()
            except:
                break

    # Create entry box
    (name := Entry(root)).pack(anchor=CENTER)
    name.bind("<Return>", connect)

    root.mainloop()
    handle_exit()


if __name__ == '__main__':
    main()
