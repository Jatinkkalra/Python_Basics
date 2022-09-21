
# For Else
# Find the first number divisible by 5, else execute "Not Found"
nums = [18, 15, 37, 45, 95]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not Found")

print()

# Prime Numbers

number = 21

for i in range(2, number):
    if number % i == 0:
        print(number, " is not a prime number")
        break
else:
    print(number, " is a prime number")

