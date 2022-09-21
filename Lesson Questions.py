# Python Tutorial

# Solving questions for each concept

# Variables

# Underscore "_"; means the output of the previous operation

x, y = 5, 6
print(x+y)

# print(_ + 12)

# r means raw string.
# /n means new line

print(r"Telusko \n Rocks")

print("Telusko \n Rocks")

# List

name = "Telusko"
# Tuples and Set

print(name[-3])


a = 15
b = 12
x = (a//4 + b**3) < 2000 and (b % 4 != 0)
print(x)

print((a//4 + b**3))

# User Input

x = int(input("Find cube of this number:"))
cube_of_a_number = x ** 3

print(cube_of_a_number)

# If, Elif, Else

q = -19
if q >= 1:
    print("positive")
else:
    print("negative")

number_1 = int(input("insert number 1: "))
number_2 = int(input("insert number 2: "))
number_3 = int(input("insert number 3: "))


Greatest_number = max(number_1, number_2, number_3)

print(Greatest_number)

# or

print(max(int(input("Insert No. 1: ")), int(input("Insert No. 2: ")), int(input("Insert No. 3: "))))

# While Loop

# Print values from 1 to 100 but skip numbers divisible by 3 or 5

i = 1
while i <= 10:
    if i % 3 != 0 and i % 5 != 0:
        print(i, "", end="")
    i += 1

print()
print()

# Pattern

j = 1

while j <= 5:
    print("# ", end="")
    k = 1
    while k <= 4:
        print("# ", end="")
        k = k + 1

    print()
    j = j + 1

print()

# For Loop

for i in range(0, 501):
    if i**2 <= 500:
        print(i**2)






