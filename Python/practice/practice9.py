class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def plus(self):
        return self.number1 + self.number2

    def minus(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def division(self):
        return self.number1 // self.number2

    def print(self):
        return print(f'# number1 = {self.number1}, number2 = {self.number2}',
        f'# 합 : {self.number1 + self.number2}',
        f'# 빼기 : {self.number1 - self.number2}',
        f'# 곱 : {self.number1 * self.number2}',
        f'# 몫 : {self.number1 // self.number2}', sep="\n")


# 문제1
calculator = Calculator(10, 5)
print(calculator.plus())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.plus())


# 문제2
calculator = Calculator(10, 5)
print(calculator.minus())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.minus())


# 문제3
calculator = Calculator(10, 5)
print(calculator.multiply())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.multiply())


# 문제4
calculator = Calculator(10, 5)
print(calculator.division())

calculator.number1 = -2
calculator.number2 = 2
print(calculator.division())


# 문제5
calculator = Calculator(10, 5)
calculator.print()

calculator.number1 = -2
calculator.number2 = 2
calculator.print()