import sqlite3
import socket
import os

HOST_IP = '127.0.0.1'
PORT = 8000

def check_database_exist(db_name):
    split_result = db_name.rsplit('.', 1)
    if ((len(split_result) == 2) and (split_result[1] == 'db')):
        if(os.path.isfile(db_name)):
            print('database exist')
        else:
            print('database not exist')
            exit()
    else:
        print("Wrong file name")
        exit()   

if __name__ == '__main__':
    database_name = 'model_state_database.db'
    check_database_exist(database_name)
    connection = sqlite3.connect(database_name)
    cursor_object = connection.cursor()
    while True:
        cursor_object.execute('''SELECT * FROM model_states where Insert_time = (select min(Insert_Time) from (SELECT Insert_Time FROM model_states where train_flag != 0))''')
        connection.commit()
        rows=cursor_object.fetchall()
        # print(len(rows))
        # print(rows)
        if(len(rows) != 0):
            if(rows[0][4] != 0):
                print("Need to Train")
                # Train
                open(str(rows[0][1]) + ".txt", "w")
                cursor_object.execute('''UPDATE model_states SET Insert_Time = CURRENT_TIMESTAMP, Device_IP = ?, client_model_dir = ?, train_flag = ? WHERE Device_Index = ?''', (rows[0][2], rows[0][3], 0, rows[0][1]))
                connection.commit()
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.connect((HOST_IP, PORT))
                server_message = "Please Download New Model"
                server.sendall(server_message.encode())
                server.close()
    connection.close()