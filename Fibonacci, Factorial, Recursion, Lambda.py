
print("#️⃣ Fibonacci Sequence")


def fibonacci(x):
    a = 0
    b = 1
    if x < 0:
        print("Invalid argument")
    elif x == 0:
        print("Insert a higher number")
    elif x == 1:
        print(a)
    elif x > 1:
        print(a, end=" ")
        print(b, end=" ")
        for i in range(2, x):
            c = a+b
            print(c, end=" ")
            a = b
            b = c
        print()


fibonacci(-1)
print()
fibonacci(0)
print()
fibonacci(1)
print()
fibonacci(2)
print()
fibonacci(17)
print()

print("#️⃣ Factorial \n")


def factorial(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    print(f)


factorial(5)
print()

print("#️⃣ Recursion \n")


def greet():
    print("Hello")
    greet()


# greet()
print()

print("#️⃣ Factorial using Recursion \n")


def recursion_in_factorial(x):
    if x == 0:
        return 1

    return x * recursion_in_factorial(x-1)


result = recursion_in_factorial(5)
print(result)
print()

print("#️⃣ Anonymous Functions | Lambda \n")

print("#️⃣ Normal way \n")


def square(a):
    return a*a


result = square(5)
print(result)
print()

print("#️⃣ Directly defining function")
print("Example 1️⃣ \n")

multiplication = lambda a: a*a

result = multiplication(5)

print(result)
print()

print("Example 2️⃣ \n")

add = lambda a, b: a+b

result = add(5, 6)

print(result)




