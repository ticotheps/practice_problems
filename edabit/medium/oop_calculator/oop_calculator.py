"""
SIMPLE OOP CALCULATOR

Create methods for the calculator class that can do the following:
    - Add two numbers.
    - Subtract two numbers.
    - Multiply two numbers.
    - Divide two numbers. 

Examples:
    - calculator = Calculator()
    - calculator.add(10,5) -> 15
    - calculator.subtract(10,5) -> 5
    - calculator.multiply(10,5) -> 50
    - calculator.divide(10,5) -> 2
"""

class Calculator:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        return num1 // num2
    
calc = Calculator('calc')
print(calc)

print(calc.add(10, 5))  # should be 3
print(calc.subtract(10, 5))  # should be 5
print(calc.multiply(10, 5))  # should be 50
print(calc.divide(10, 5))  # should be 2