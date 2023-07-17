import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def sqrt(num):
    return math.sqrt(num)

def mod(num1, num2):
    return num1 % num2

def exponent(num1, num2):
    return num1 ** num2