import socket
# Define the server's IP address and port
SERVER_IP = '127.0.0.1'  # localhost
SERVER_PORT = 12345

# Define the test message to be sent from the client to the server
TEST_MESSAGE = "Hello, server! This is a test message."

def server():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the server address and port
        server_socket.bind((SERVER_IP, SERVER_PORT))

        # Listen for incoming connections
        server_socket.listen()

        print("Server is listening on {}:{}".format(SERVER_IP, SERVER_PORT))

        # Accept a connection from a client
        connection, client_address = server_socket.accept()

        with connection:
            print("Connected to client:", client_address)

            # Receive data from the client
            data = connection.recv(1024)

            print("Received message from client:", data.decode())

            # Send a response back to the client
            connection.sendall(b"Message received. Connection test successful.")

def client():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect the socket to the server's IP address and port
        client_socket.connect((SERVER_IP, SERVER_PORT))

        # Send the test message to the server
        client_socket.sendall(TEST_MESSAGE.encode())

        # Receive a response from the server
        data = client_socket.recv(1024)

        print("Received message from server:", data.decode())

if __name__ == "__main__":
    # Start the server in a separate thread
    # You can run the client and server in different terminals
    import threading
    server_thread = threading.Thread(target=server)
    server_thread.start()

    # Run the client
    client()
