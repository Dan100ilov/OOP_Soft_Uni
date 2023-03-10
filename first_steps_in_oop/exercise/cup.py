class Cup:
    def __init__(self, size:int, quantity:int):
        self.size = size
        self.quantity = quantity

    def fill(self, new_q):
        if self.quantity+new_q < self.size:
            self.quantity += new_q
            return self.quantity

    def status(self):
        return self.size-self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
