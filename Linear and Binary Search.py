
print("#️⃣#️⃣ Linear Search \n")

list = [5, 8, 4, 6, 9, 2]
n = 6

def search(list, x):
    for i in range(len(list)-1):    # for i in list:
        if list[i] == n:            # if i == n
            print("Found at index no:", i)  # list[i]
            break
    else:
        print("Not Found")

search(list, n)
print()

print("-----------------------------")
print("#️⃣#️⃣ Binary Search")

values = [4, 7, 8, 12, 45, 99]  # List should be sorted for binary search
m = 458

def binary_search(list, x):
    l = 0
    u = len(list)-1 # Important

    while l <= u:
        mid = (l+u) // 2

        if values[mid] == m:
            print("Found at index no:", mid)
            break
        else:
            if values[mid] < m:
                l = mid+1   # Important
            else:
                u = mid-1   # Important
    else:
        print("Not Found")

binary_search(values, m)