import socket

CLIENT_IP = '140.124.182.40'
PORT = 8001

client_socket = socket.socket(socket.AF_INET)
client_socket.bind((CLIENT_IP, PORT))
client_socket.listen(10)
while True:
    connection, address = client_socket.accept()
    message_from_server = str(connection.recv(4096), encoding='utf-8')
    print("Server message is : ", v)
