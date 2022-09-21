
print("#️⃣#️⃣ Bubble Sort")

list = [3, 65, 34, 89, 76, 54, 4]

def sort(x):
    for i in range(len(list)-1, 0, -1):     # Or: len(list)
        for j in range(i):                  # range(i-1)
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]   # OR: temp = list[j]
    print(list)                                           # list[j] = list[j+1]
                                                          # list[j+1] = temp

sort(list)
print()

print("----------------------------------")
print("#️⃣#️⃣ Selection Sort")

nums = [287, 46, 534, 64, 343, 32, 3, 10]

def sorting(x):
    for i in range(len(nums)):
        minimum_value = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minimum_value]:
                nums[j], nums[minimum_value] = nums[minimum_value], nums[j]
    print(nums)

sorting(nums)
