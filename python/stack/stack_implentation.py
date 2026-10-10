#implement stack using the dynamic array
# it should have the 3 buttons one for insert , delete and peak
# it should follow the LIFO scematic maner

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from stack.")
            return item
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            item = self.stack[-1]
            print(f"Top item is: {item}")
            return item
        else:
            print("Stack is empty. No top item.")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack) 
#calling the stack class
if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")