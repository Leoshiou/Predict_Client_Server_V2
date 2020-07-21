import socket
HOST_IP = '127.0.0.1'
PORT = 8000
DEVICE_ID = '1'
MODEL_DIR = 'Temp_Client_Folder'

# Train Flag
# 0 => Normal
# 1 => Finetune
# 2 => Retrain

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_IP, PORT))
client_message = DEVICE_ID + '_' + HOST_IP + '_' + MODEL_DIR + '_' + '1'
client.sendall(client_message.encode())
client.close()