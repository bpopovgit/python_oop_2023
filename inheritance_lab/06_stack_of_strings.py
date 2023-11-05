class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        if not isinstance(element, str):
            raise ValueError("Element is not a string, please add only strings")
        self.data.append(element)

    def pop(self):
        element = self.data.pop()
        return element

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not any(self.data)

    def __str__(self):
        reversed_data = list(reversed(self.data))
        return f'[{", ".join(reversed_data)}]'


stack = Stack()
print(stack.is_empty())
print(stack)
stack.push('asd')
stack.push('hello')
print(stack.is_empty())
print(stack)
print(stack.pop())
print(stack)
