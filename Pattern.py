
print("Pattern 1️⃣")
for i in range(1, 5):
    print("# " * 4)

print()

print("Pattern 2️⃣")
for j in range(1, 5):
    print("# " * j)

print()

print("Pattern 3️⃣")
for k in range(4, 0, -1):
    print("# " * k)

print()

print("Pattern 4️⃣")
for q in range(1, 5):
    for p in range(q, 5):
        print(p, end="")
    print()

print()

print("Pattern 4️⃣, Method 2")
for d in range(4):
    for e in range(4-d):
        print(d+e+1, end="")
    print()

print()

print("Pattern 5️⃣")
string1 = "ABCD"
string2 = "OPQR"

for u in range(0, 4):
    print(string1[:u+1]+string2[u+1:])

print()
print("Simpler example of pattern 5️⃣ method")

s = "youtube"
t = "my"

print(s)
print(t[:2]+s[3:])

print()

print("Pattern 6️⃣")
print("Each Letter of JATIN")

print()
print("Method 1: only using and/or; ==/!=")  # Both == or != works; same line with "or" operator also works
for row in range(0, 7):
    for col in range(0, 7):
        if (col == 3) or ((row == 4 and row == 5 and row == 6) and col == 0):
            print("J ", end="")
        elif (row == 0) or ((col != 4 and col != 5 and col != 6) and row == 6):
            print("J ", end="")
        else:
            print("  ", end="")
    print()

print()

print("Method 2: using the 'in' function")

for row in range(0, 7):
    for col in range(0, 7):
        if row == 0 or col == 3:
            print("J ", end="")
        elif (row == 6 and (col in (0, 1, 2))) or (col == 0 and (row in (4, 5, 6))):
            print("J ", end="")
        else:
            print("  ", end="")
    print()

print()

for row in range(0, 7):
    for col in range(0, 7):
        if row != 0 and (col == 0 or col == 6):
            print("A ", end="")
        elif (row == 0 or row == 3) and (col != 0 and col != 6):
            print("A ", end="")
        else:
            print("  ", end="")
    print()

print()

print("Method 2")
for row in range(0, 7):
    for col in range(0, 7):
        if (row in (1, 2, 3, 4, 5, 6)) and (col in (0, 6)):
            print("A ", end="")
        elif row == 0 and (col in (1, 2, 3, 4, 5)):
            print("A ", end="")
        elif row == 3:
            print("A ", end="")
        else:
            print("  ", end="")
    print()


print()

for row in range(0, 7):
    for col in range(0,7):
        if row == 0 or col == 3:
            print("T ", end="")
        else:
            print("  ", end="")
    print()

print()

for row in range(0, 7):
    for col in range(0, 7):
        if row == 0 or row == 6 or col == 3:
            print("I ", end="")
        else:
            print("  ", end="")
    print()

print()

for row in range(0, 7):
    for col in range(0, 7):
        if col == 0 or col == 6 or (row == col):
            print("N ", end="")
        else:
            print("  ", end="")
    print()

print()

for row in range(0, 5):
    for col in range(0, 29):
        if col == 2 or (row == 0 and col < 5) or (row == 4 and (0 <= col <= 2)) or (col == 0 and row == 3):
            print("J ", end="")
        elif (row == 0 and 6 < col < 10) or ((col == 6 or col == 10) and row != 0) or (row == 2 and 5 < col < 11):
            print("A ", end="")
        elif (row == 0 and 11 < col < 17) or col == 14:
            print("T ", end="")
        elif ((row == 0 or row == 4) and 17 < col < 23) or col == 20:
            print("I ", end="")
        elif col == 24 or col == 28 or (row == 1 and col == 25) or (row == 2 and col == 26) or (row == 3 and col == 27):
            print("N ", end="")
        else:
            print("  ", end="")
    print()
