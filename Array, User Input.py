
from array import *

vals = array('i', [1, 3, -5, 7, 9])

print(vals)
print()

print(vals.buffer_info())  # (Address, Size/Number of values)
print()

print(vals.typecode)
print()

vals.reverse()
print(vals)
print()

print(vals[0])
print()

# Code to print all values separately

# Method 1

print("Method 1️⃣")
for x in range(0, 5):
    print(vals[x])
print()

# Method 2

print("Method 2️⃣")
for y in range(len(vals)):
    print(vals[y])
print()

# Method 3

print("Method 3️⃣")
for z in vals:
    print(z)
print()

# Method 4 (using while loop)
print("Method 4️⃣: while loop")

i = 0
while i < len(vals):
    print(vals[i])
    i += 1
print()

# New Array
print("▶️New Array")

newArr = array(vals.typecode, (a**2 for a in vals))

for p in newArr:
    print(p)
print()

# Characters in array

print("▶️Characters in Array")

char = array('u', ['a', 'e', 'i', 'o'])
print(char)
print()

for q in char:
    print(q)
print()

# Assignment Questions

print("#️⃣ Assignment Questions")
print()

print("Question 1️⃣")
print(sorted(newArr))
print()

print("Question 2️⃣")

# from math import *
# print(factorial(vals[i]))

# User Input

print("#️⃣ User Input in Array")

length = int(input("Enter the length of the Array "))

arr = array('i', [])

for x in range(length):
    vals = int(input("Enter the next array "))
    arr.append(vals)

print(arr)

# Finding the index number of an array using user input

searched_int = int(input("Enter the number you want the index no of "))

print("Method 1️⃣: Manual. Using Loop to check with each array value")

k = 0
for y in arr:
    if searched_int == y:
        print(k)
    else:
        k += 1

print()

print("Method 2️⃣: Function")

print(arr.index(searched_int))
print()

# Assignment Questions

print("#️⃣ Assignment Questions")

print("Question 1️⃣")
# Create an array with 5 values & delete the value at index no. 2 without using in-built function

# Array of 5 values using input

arr2 = array("i", [])
length_arr2 = int(input("Enter the length of array "))

for t in range(length_arr2):
    array_elements = int(input("Enter an element "))
    arr2.append(array_elements)
print(arr2)

# Deleting 2nd value

for p in range(len(arr2)):
    if p == 1:
        del arr2[1]
    else:
        pass
print(arr2)

print("Question 2️⃣")
# write a code to reverse an array without using in-built function

arr3 = array('i', [23, 54, 53, 52, 51])

arr4 = array('i', [])
for j in range(4, -1, -1):
    arr4.append(arr3[j])
print(arr4)
