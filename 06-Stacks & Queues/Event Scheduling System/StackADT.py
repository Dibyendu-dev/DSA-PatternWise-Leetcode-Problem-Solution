class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def contains(self, item):
        return item in self.items

    def __str__(self):
        if self.is_empty():
            return "Waitlist is empty."
        result = "Waitlist (Top → Bottom):\n"
        for name in reversed(self.items):
            result += name + "\n"
        return result.strip()