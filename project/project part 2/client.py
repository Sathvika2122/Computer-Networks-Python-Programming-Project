import socket

def client_program():
    host = socket.gethostname()  # As both code is running on the same PC
    port = 5000  # Socket server port number

    client_socket = socket.socket()  # Instantiate
    client_socket.connect((host, port))  # Connect to the server

    message = input(" -> ")  # Take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # Send message
        data = client_socket.recv(1024).decode()  # Receive response

        print('Received from server: ' + data)  # Show in terminal

        message = input(" -> ")  # Again take input

    client_socket.close()  # Close the connection

if __name__ == '__main__':
    client_program()

