
# Six ways to create an array in numpy: array(),linspace(), logspace(), arange(), zeros(), ones()

from numpy import *

# array()

arr = array([1, 2, 3, 4, 5])
print(arr)
print(arr.dtype)
print()

arr = array([1, 2, 3, 4, 5.0])
print(arr)
print(arr.dtype)
print()

arr = array([1, 2, 3, 4, 5.0], int)
print(arr)
print(arr.dtype)
print()

arr = array([1, 2, 3, 4, 5], float)
print(arr)
print(arr.dtype)
print()

# linspace()

arr1 = linspace(0, 4, 6)  # 16 / end is included here. 10 is not a step, but no. of paths.
print(arr1)
print()

arr2 = linspace(0, 4)  # By default, the third element is 50 steps)
print(arr2)
print()

# arange()
arr3 = arange(1, 10, 3)
print(arr3)
print()

# logspace()
arr4 = logspace(1, 40, 5)
print(arr4)
print()

# zeros()
arr5 = zeros(5)  # print number of zeros in an array
print(arr5)
print()

# ones()
arr6 = ones(5)  # print number of ones in an array
print(arr6)
print()

arr6 = ones(5, int)
print(arr6)
print()

print("#️⃣ Operation on Array")
print("#️⃣ Adding 5 to each value of an array")

arrA = array([1, 2, 3, 4, 5])
print(arrA)
print()

print("Method 1️⃣: Manually using loop")

arrB = ([])
arrB.append(arrA+5)
print(arrB)
print()

print("Method 2️⃣: Operation")

arrB = arrA + 5
print(arrB)
print()

print("#️⃣ Adding two arrays(aka Vectorised Operation): arrA + arrB")
arrC = arrA + arrB
print(arrC)
print()

print("#️⃣ Mathematical Operations")
print("Sin, Cos, log, sqrt, sum,min, max, sort, concatenate")
print(sin(arrC))
print(cos(arrC))
print(log(arrC))
print(sqrt(arrC))
print(sum(arrC))
print(min(arrC))
print(max(arrC))
print(sort(arrC))
print(concatenate([arrA, arrB]))
print()

print("#️⃣ Copying an Array")
print()

arrD = array([2, 4, 6, 8])
print(arrD)
print()

print("#️⃣ Aliasing")
arrE = arrD
arrD[3] = 10

print(arrD)
print(arrE)
print(id(arrD))
print(id(arrE))
print()

print("#️⃣ Shallow Copy")

arrE = arrD.view()
arrD[2] = 12

print(arrD)
print(arrE)
print(id(arrD))
print(id(arrE))
print()

print("#️⃣ Deep Copy")
arrE = arrD.copy()
arrD[1] = 18

print(arrD)
print(arrE)
print(id(arrD))
print(id(arrE))
print()

print("#️⃣ Assignment Questions")
print()
print("Question 1️: Code to add 2 arrays using forloop")

arrP = array([1, 2, 3, 4, 5])
arrQ = array([6, 7, 8, 9, 10])

print("Method 1️⃣")
arrR = array([i for i in arrP + [j for j in arrQ]])
print(arrR)
print()

print("Method 2️⃣")
arrS = zeros(5, int)
for h in range(len(arrP)):
    arrS[h] = arrP[h]+arrQ[h]
print(arrS)
print(type(arrS))
print()


