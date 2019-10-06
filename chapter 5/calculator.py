
# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def add(self, num):
#         self.result += num
#         return self.result
class Calculator:
    def __init__(self):
        self.first_number=0
        self.second_number=0

    def set_data(self, first, second):
        self.first_number = first
        self.second_number = second
        return True
    
    def add(self):
        return self.first_number + self.second_number

    def div(self):
        return self.first_number / self.second_number
    
    def mul(self):
        return self.first_number * self.second_number

    def minus(self):
        return self.first_number - self.second_number

class Calculator_more(Calculator):
    def pow(self):
        return self.first_number ** self.second_number
    
    def div(self):
        if self.first_number == 0 or self.second_number == 0:
            return 0
        else:
            return 0


def main():
    cal1 = Calculator()
    cal1.set_data(2, 3)
    print(cal1.add())
    print(cal1.mul())
    print(cal1.div())
    print(cal1.minus())

    cal2 = Calculator_more()
    cal2.set_data(2,0)
    print(cal2.pow())
    print(cal2.div())

if __name__ == "__main__":
    main()