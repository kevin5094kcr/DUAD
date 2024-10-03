class Node:
    data = str
    next = "Node"

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # Points to the previous node     


class Deque:
    def __init__(self):
        self.head = None 
        self.tail = None  # The back of the deque

    
    def push_left(self, data): # This method adds a new node to the front
        new_node =  Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head # New node points to the current head
            self.head.prev = new_node  # The current head points back to the new node
            self.head = new_node

    
    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail # New node points to the back of the tail
            self.tail.next = new_node # The current tail points to the new node
            self.tail = new_node

    def pop_left(self):
        if self.head is None: # If deque is empty
            return None
        removed_node = self.head # Store the node to be removed
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next # Move head to the next node
            self.head.prev = None
        return removed_node.data
    
    def pop_right(self):
        if self.tail is None: 
            return None
        removed_node = self.tail
        if self.head == self.tail: # If there's only one node 
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # Move tail to the previous node
            self.tail.next = None # Set the new tail next to None
        return removed_node.data
    
    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

deque = Deque()

deque.push_left("Hello, i'm the new node.")
deque.push_right("Hello, now i'm the newest node.")
deque.push_left("Hello world!!")
deque.push_right("Hi Deque.")

print("Deque after push operations:")
deque.print_structure()

# Remove elements from the front and back
print("Deque after push: ")
deque.print_structure()

# Remove elements from the front and the back
deque.pop_left()
deque.pop_right()

print("Deque after pop: ")
deque.print_structure()



