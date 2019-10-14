class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
    
    def minus(self, val):
        self.value-= val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        if val > 50:
            val = 50
        self.value += val
    