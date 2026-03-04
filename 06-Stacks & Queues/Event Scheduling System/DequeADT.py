class Deque:
    def __init__(self, capacity=5):
        self.items = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.capacity

    def add_front(self, item):
        if not self.is_full():
            self.items.insert(0, item)
            return True
        return False

    def add_back(self, item):
        if not self.is_full():
            self.items.append(item)
            return True
        return False

    def remove_back(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def contains(self, item):
        return item in self.items

    def __str__(self):
        if self.is_empty():
            return "Registration List is empty."
        result = "Registration List (Front → Back):\n"
        for name in self.items:
            result += name + "\n"
        return result.strip()