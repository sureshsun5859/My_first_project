class Node:
    def __init__(self, data):
        self.data = data
        # Points to the next node; None means this is the last node.
        self.next = None


class LinkedList:
    def __init__(self):
        # The head is the first node and the tail is the last node.
        # Both are None while the list is empty.
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            # The new node is both the first and last node.
            self.head = new_node
            self.tail = new_node
        else:
            # Link the old last node to the new one, then move the tail.
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        # Put the new node before the current first node.
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            # If the list was empty, this node is also the last node.
            self.tail = new_node

    def display(self):
        current = self.head
        # Follow each next link until there are no more nodes.
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#example 
ll = LinkedList()
ll.append(1)

ll.append(2)
ll.append(3)
ll.append("suresh")
ll.prepend("thiragabathina")
ll.display()  # Output: 1 -> 2 -> 3 -> None