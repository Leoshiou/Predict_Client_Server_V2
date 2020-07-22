# Predict_Client_Server_V2
Client Server architecture Trajectory Prediction V2

## System Architecture
![image](https://github.com/Leoshiou/Predict_Client_Server_V2/blob/master/20200423_client-server_%E6%9E%B6%E6%A7%8B.jpg)

## Database Structure
Server Model State Database Structure
```sql
'''CREATE TABLE model_states(Insert_Time TIMESTAMP, Device_Index integer, Device_IP char(50), client_model_dir char(100), train_flag integer, PRIMARY KEY(Device_Index))'''
```
## Server
1. Connect model state database
2. Select the earliest state which the Train_Flag is not 0


## socket_Server
1. Create model state database
2. Create socket
3. Stay listen
4. Receive message and split by "_"
5. Insert the message into database (Update the information of the existed device_id, when it's **Train_Flag** = 0)

## Client
Set DEVICE_ID, HOST_IP, MODEL_DIR, Train_Flag
client_message = **DEVICE_ID**___**HOST_IP**___**MODEL_DIR**___**Train_Flag**

## socket_Client
1. Stay listen
2. Download new model from Server

## Operate Flow (Simulation)
1. Start **socket_Server**
2. Start **socket_Client**
3. Start **Server**
4. Send model state information through **Client**