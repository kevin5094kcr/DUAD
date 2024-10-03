class Node: 
    data = str
    next = "Node"
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    head = Node 

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def push(self, new_node):
        new_node.next = self.head
        self.head = new_node


    def pop(self):
        if self.head is None:
            return None
        removed_node = self.head
        self.head = self.head.next
        return removed_node.data
        
first_node = Node("Hello world!")
stack = Stack(first_node)

second_node = Node("I'm second")
stack.push(second_node)

third_node = Node("I'm third")
stack.push(third_node)


stack.print_structure()

print("Popped item:", stack.pop())


print("Stack after popping:")
stack.print_structure()