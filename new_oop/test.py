baseSalary = 25_000
overtime = 8.33
rate = 16.67

# procedural
# def getWage(baseSalary, overtime, rate):
#     return baseSalary + overtime * rate

# wage = getWage(baseSalary, overtime, rate)
# print(round(wage, 2))

# object oriented
class Employee:
    def __init__(self, baseSalary, overtime, rate) -> None:
        self.baseSalary = baseSalary
        self.overtime = overtime
        self.rate = rate

    def getWage(self):
        return self.baseSalary + self.overtime * self.rate

employee1 = Employee(baseSalary, overtime, rate)
wage = employee1.getWage()
print(round(wage, 2))
