class Router:
    def __init__(self, name):
        self.name = name
        self.table = {}  # routing table
        self.neighbours = {}  # neighbour: cost

        # add itself to table
        self.table[name] = (name, 0)  # next_hop, cost

    def add_neighbour(self, neighbour, cost):
        self.neighbours[neighbour] = cost
        self.table[neighbour] = (neighbour, cost)

    def update_table(self, neighbour_name, neighbour_table):
        cost_to_neighbour = self.neighbours[neighbour_name]

        for destination in neighbour_table:
            next_hop, neighbour_cost = neighbour_table[destination]

            new_cost = cost_to_neighbour + neighbour_cost

            if destination not in self.table:
                self.table[destination] = (neighbour_name, new_cost)

            else:
                current_cost = self.table[destination][1]
                if new_cost < current_cost:
                    self.table[destination] = (neighbour_name, new_cost)

    def print_table(self):
        print(f"\nRouting Table for {self.name}")
        print("Destination | Next Hop | Cost")

        for destination in self.table:
            next_hop, cost = self.table[destination]
            print(f"{destination}           {next_hop}         {cost}")

    # Create routers
A = Router("A")
B = Router("B")
C = Router("C")

# Define connections
A.add_neighbour("B", 1)

B.add_neighbour("A", 1)
B.add_neighbour("C", 1)

C.add_neighbour("B", 1)

# Print initial tables
# Issues here
print("INITIAL TABLES")
A.print_table()
B.print_table()
C.print_table()

# Simulate updates
print("\nUPDATING TABLES...")

A.update_table("B", B.table)
C.update_table("B", B.table)

# Print updated tables
print("\nUPDATED TABLES")
A.print_table()
B.print_table()
C.print_table()