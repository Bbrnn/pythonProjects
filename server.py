import socket

def main():
    # Step 1: Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2: Bind the socket to a specific location (port, IP address)
    server_address = ('0.0.0.0', 12345)  # 0.0.0.0 means to listen on all available interfaces
    server_socket.bind(server_address)
    print(f'Server is bound to {server_address}')

    # Step 3: Listen for incoming messages
    server_socket.listen(5)  # The argument specifies the maximum number of queued connections
    print('Server is listening for incoming connections')

    while True:
        # Step 4: Accept connection from incoming messages
        client_socket, client_address = server_socket.accept()
        print(f'Connection from {client_address} has been established.')

        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if data:
                print(f'Received data: {data.decode()}')

                # Optionally, send a response back to the client
                client_socket.sendall(b'Message received')
            else:
                print('No data received from the client.')

        finally:
            # Close the client connection
            client_socket.close()
            print(f'Connection from {client_address} has been closed.')

if __name__ == '__main__':
    main()

