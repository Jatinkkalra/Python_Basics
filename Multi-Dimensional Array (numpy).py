
from numpy import *

arr1 = array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print(arr1)
print()

print("#️⃣Type")
print(arr1.dtype)

print("#️⃣ Dimensions")
print(arr1.ndim)

print("#️⃣ Shape (rows, columns)")
print(arr1.shape)

print("#️⃣ No of elements")
print(arr1.size)
print()

print("#️⃣ Converting to 1 dimensional")
arr2 = arr1.flatten()
print(arr2)
print()

print("#️⃣ Converting to 2 dimensional")
arr3 = arr2.reshape(3, 4)
print(arr3)
print()

print("#️⃣ Converting to 3 dimensional")
arr4 = arr2.reshape(2, 3, 2)
print(arr4)
print()

print("#️⃣ Converting 2d array to matrix")
m = matrix(arr1)
print(m)
print()

print("#️⃣ Directly creating a matrix")

n = matrix('1 2 3; 4 5 6; 7 8 9')
print(n)
print()

o = matrix('1 2; 3 4; 5 6; 7 8')
print(o)
print()

print("#️⃣ Diagonal Elements")
print(diagonal(n))
print()

print(diagonal(o))
print()

print("#️⃣ Min and Max Values")
print(m.max())
print(m.min())
print()

print("#️⃣ Adding and Multiplication of Matrix")
j = matrix('1 2 3; 4 5 6; 7 8 9')
k = matrix('1 2 9; 4 5 7; 9 8 7')

print(j+k)
print()

print(j*k)
print()

print("#️⃣ Assignment Questions")



