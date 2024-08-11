import socket

def main():
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port to connect to
    server_address = ('localhost', 12345)

    # Connect to the server
    client_socket.connect(server_address)

    try:
        # Send a message to the server
        message = "Hello, Server!"
        client_socket.sendall(message.encode())

        # Receive the response from the server
        response = client_socket.recv(1024)
        print(f'Received response from the server: {response.decode()}')

    finally:
        # Close the connection
        client_socket.close()

if __name__ == '__main__':
    main()

