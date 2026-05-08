import socket
import json
# Clone client_C
HOST = "127.0.0.1"
PORT = 3110

routing_table = {
    "A": ["A", 0],
    "B": ["B", 1]
}

data = {
    "router": "A",
    "table": routing_table
}

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send(json.dumps(data).encode())

client.close()