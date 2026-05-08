import socket
import json 
#Easier readability

HOST = "127.0.0.1"
PORT = 3110 #Change port number

routing_table = {
    "C": ["C", 0],
    "B": ["B", 1]
}

data = {
    "router": "C",
    "table": routing_table
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

#Issue here
client.send(json.dumps(data).encode())

client.close()