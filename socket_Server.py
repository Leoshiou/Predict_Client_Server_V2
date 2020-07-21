import socket
import sqlite3
import os

HOST = '127.0.0.1'
PORT = 8000

def create_model_state_database(db_name):
    split_result = db_name.rsplit('.', 1)
    if ((len(split_result) == 2) and (split_result[1] == 'db')):
        print("Corrent")
        os.remove(db_name)
        connection = sqlite3.connect(db_name)
        cursor_object = connection.cursor()
        cursor_object.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name = 'model_states' ''')
        connection.commit()
        if cursor_object.fetchone()[0] == 1:
            print('Table exists')
        else:
            print('Table is empty')
            cursor_object.execute('''CREATE TABLE model_states(Insert_Time TIMESTAMP, Device_Index integer, Device_IP char(50), client_model_dir char(100), train_flag integer, PRIMARY KEY(Device_Index))''')
            connection.commit()
        connection.close()
    else:
        print("Wrong file name")
        exit()

if __name__ == '__main__':
    database_name = 'model_state_database.db'
    create_model_state_database(database_name)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    while True:
        connection, address = server.accept()
        client_message = str(connection.recv(4096), encoding='utf-8')
        print("Client message is : ", client_message)
        message_split = client_message.split("_")
        connection = sqlite3.connect(database_name)
        cursor_object = connection.cursor()
        cursor_object.execute('''SELECT * FROM model_states WHERE Device_Index=?''', (message_split[0]))
        connection.commit()
        rows=cursor_object.fetchall()
        if(len(rows) == 0):
            print("Insert")
            cursor_object.execute('''INSERT INTO model_states VALUES (CURRENT_TIMESTAMP,?,?,?,?)''', (message_split[0], message_split[1], message_split[2], message_split[3]))
            connection.commit()
        else:
            if(rows[0][4] == 0):
                print("Update")
                cursor_object.execute('''UPDATE model_states SET Insert_Time = CURRENT_TIMESTAMP, Device_IP = ?, client_model_dir = ?, train_flag = ? WHERE Device_Index = ?''', (message_split[1], message_split[2], message_split[3], message_split[0]))
                connection.commit()
    connection.close()