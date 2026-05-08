import socket
import json
import time

HOST = "127.0.0.1"
PORT = 3110
# Change port number
# Router B routing table
routing_table = {
    "B": ("B", 0),
    "A": ("A", 1),
    "C": ("C", 1)
}
#Add cost
neighbours = {
    "A": 1,
    "C": 1
}
# Set iteration
iteration = 0

def update_table(neighbour_name, neighbour_table):
    cost_to_neighbour = neighbours[neighbour_name]

    for destination in neighbour_table:
        next_hop, neighbour_cost = neighbour_table[destination]

        new_cost = cost_to_neighbour + neighbour_cost

        if destination not in routing_table:
            routing_table[destination] = (neighbour_name, new_cost)
            print(f"New route added: {destination} via {neighbour_name} cost {new_cost}")

        else:
            current_cost = routing_table[destination][1]
            if new_cost < current_cost:
                routing_table[destination] = (neighbour_name, new_cost)
                print(f"Updated route: {destination} via {neighbour_name} cost {new_cost}")

def print_table():
    print("\nRouter B Routing Table")
    print("Destination | Next Hop | Cost")
    for dest in routing_table:
        nh, cost = routing_table[dest]
        print(f"{dest}           {nh}         {cost}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Router B waiting for connections...")

while True:
    conn, addr = server.accept()

    data = conn.recv(1024).decode()

    if data:
        received = json.loads(data)
        neighbour_name = received["router"]
        table = received["table"]

        iteration += 1
        print(f"\n--- Iteration {iteration} ---")

        print(f"Received table from Router {neighbour_name}:")
        print(table)

        update_table(neighbour_name, table)
        print_table()

    conn.close()