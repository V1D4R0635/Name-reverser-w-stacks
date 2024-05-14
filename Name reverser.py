class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def reverse_name(name):
    stack = Stack()

    for char in name:
        stack.push(char)

    reversed_name = ""
    while not stack.is_empty():
        reversed_name += stack.pop()

    return reversed_name


def main():
    name = input("Enter name: ")
    reversed_name = reverse_name(name)
    print(f"Reversed name: {reversed_name}")


if __name__ == "__main__":
    main()
