import socket

def server_program():
    # Get the hostname
    host = socket.gethostname()
    port = 5000  # Initiate port no above 1024

    server_socket = socket.socket()  # Get instance
    # Look closely. The bind() function takes the tuple as argument
    server_socket.bind((host, port))  # Bind host address and port together

    # Configure how many clients the server can listen to simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # Accept new connection
    print("Connection from: " + str(address))
    while True:
        # Receive data stream. It won't accept data packets greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # If data is not received, break
            break
        print("From connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # Send data to the client

    conn.close()  # Close the connection

if __name__ == '__main__':
    server_program()

