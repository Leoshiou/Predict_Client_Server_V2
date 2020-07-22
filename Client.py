import socket
SERVER_IP = '140.124.182.48'
PORT = 8000
DEVICE_ID = '1'
MODEL_DIR = 'TempClientFolder'

# Train Flag
# 0 => Normal
# 1 => Finetune
# 2 => Retrain

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
client_message = DEVICE_ID + '_' + HOST_IP + '_' + MODEL_DIR + '_' + '2'
client_socket.sendall(client_message.encode())
client_socket.close()
