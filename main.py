
# Python tutorial

from array import *
from numpy import *

print("#️⃣ Assignment Questions \n")

print("Question 2️⃣: Find maximum value from an array without using in-built function \n")

print("#️⃣ Write a code to multiply 2 matrices using 2d array and using for loop \n")
print("Method 1️⃣: Using 2d array \n")
print("Method 2️⃣: Using for loop \n")

print("#️⃣ Write a code to find the fibonacci number lower than 100 \n")  # 89

print("#️⃣ Factorial using Recursion \n")


def recursion_in_factorial(x):  # learn about return and result usage
    if x == 0:
        return 1

    return x * recursion_in_factorial(x-1)


result = recursion_in_factorial(5)
print(result)

print("#️⃣ Methods preferred over __init__ / in-built attributes in a new class")


class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 18

    def change(self):
        self.age = 60


c1 = Computer()
c2 = Computer()

c2.change()
print(c1.name, c1.age)
print(c2.name, c2.age)
print()
