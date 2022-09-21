
# Use cases of Lambda: Filter(); Map(); Reduce()

nums = [3, 4, 5, 6, 7, 8, 9]

print("#️⃣ filter(). | It checks True or False of statements \n")
print("Method 1️⃣: Using function")


def even(x):
    return x % 2 == 0   # If true, it will be returned/included in the function


even_no = list(filter(even, nums))
print(even_no, "\n")

print("Method 2️⃣: Using lambda")

even_no_2 = list(filter(lambda x: x % 2 == 0, nums))
print(even_no_2, "\n")

print("#️⃣ map(). | Applies function to iterables. Ex: values in a list\n")

print("Method 1️⃣: Using function")


def adding_2(y):
    return y+2


added_2 = list(map(adding_2, even_no))
print(added_2, "\n")

print("Method 2️⃣: Using lambda")

added_2_2 = list(map(lambda y: y + 2, even_no))
print(added_2_2)

print("#️⃣ reduce(). | Function applied to have one value as outcome \n "
      "| Two values are used at a time \n"
      "| Cane be used to find factorial \n")


from functools import reduce
print("Method 1️⃣: Using function")


def sum(a, b):
    return a + b


sum_of_all = reduce(sum, added_2)
print(sum_of_all, "\n")

print("Method 2️⃣: Using lambda")

sum_of_all_2 = reduce(lambda a, b: a+b, added_2)
print(sum_of_all_2, "\n")

print("Finding factorial using lambda")

factorial_of_5 = reduce(lambda a, b: a*b, range(1, 6))
print(factorial_of_5, "\n")

print("Finding factorial through user input and using lambda")

factorial_of_x = reduce(lambda a, b: a*b, range(1, int(input("Find Factorial of: "))+1))
print(factorial_of_x)
