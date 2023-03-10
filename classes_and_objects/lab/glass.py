class Glass:
    initial_capacity = 0
    capacity = 250

    def __init__(self):
        self.content = self.initial_capacity

    def fill(self, param):
        if param <= self.calculate_space_left():
            self.content += param
            return f"Glass filled with {param} ml"
        else:
            return f"Cannot add {param} ml"

    def empty(self):
        self.content = 0
        return f"Glass is now empty"

    def calculate_space_left(self):
        return self.capacity - self.content

    def info(self):
        return f"{self.calculate_space_left()} ml left"


content = Glass()
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
