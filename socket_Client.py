import socket

HOST = '127.0.0.1'
PORT = 8001

server = socket.socket(socket.AF_INET)
server.bind((HOST, PORT))
server.listen(10)
while True:
    connection, address = server.accept()
    client_message = str(connection.recv(4096), encoding='utf-8')
    print("Client message is : ", client_message)