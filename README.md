# Predict_Client_Server_V2
Client Server architecture Trajectory Prediction V2

## System Architecture
![image](https://github.com/Leoshiou/Predict_Client_Server_V2/blob/master/20200423_client-server_%E6%9E%B6%E6%A7%8B.jpg)

## Database Structure
Server Model State Database Structure
```sql
'''CREATE TABLE model_states(Insert_Time TIMESTAMP, Device_Index integer, Device_IP char(50), client_model_dir char(100), train_flag integer, PRIMARY KEY(Device_Index))'''
```

## socket_Server
1. Create model state database
2. Create socket
3. Stay listen
4. Receive message and split by "_"
5. Insert the message into database (Update the information of the existed device_id, when it's train_flag = 0)
