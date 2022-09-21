
print("#️⃣ Functions in Python")
print()


def greet():
    print("Hello")
    print("Good Morning")


greet()
print()

print("#️⃣ Adding 2 numbers")


def add(x, y):
    z = x + y
    print(z)


add(5, 4)
print()

print("#️⃣ Returning 2 values: adding and subtracting 2 numbers")


def add_sub(a, b):
    c = a+b
    d = a-b
    return c, d


result1 = add_sub(5, 4)
print(result1)
print()

print("#️⃣ Returning results separately")

result1, result2 = add_sub(5, 4)
print(result1, result2)
print()

print("#️⃣ Function Arguments")


def inside(q):
    p = 8
    print("p_inside_function is", p)


p = 10
print("p_outside_function is", p)

inside(10)
print()


def inside_2(s):
    print(id(s))
    s = 18
    print("s_inside_function is", s)
    print(id(s))


r = 20
print(id(r))
print()

inside_2(r)
print()

print("r_outside_function is", r)
print(id(r))
print()

print("#️⃣ Types of Argument")


def add(m, n):  # Formal Arguments
    o = m+n
    print(o)


add(5, 6)  # Actual Arguments
print()

print("#️⃣ Position Argument")


def person(name, age):
    print(name)
    print(age)


person('navin', 28)  # Position matters
print()

print("#️⃣ Keyword Argument")


def person(name, age):
    print(name)
    print(age)


person(age=28, name='navin')
print()

print("#️⃣ Default Argument | Used last in sequence")


def person(name, age=18):
    print(name)
    print(age)


person('navin')
print()

print("Example 2️⃣")


def person(name, age=18):
    print(name)
    print(age)


person('navin', 30)
print()

print("#️⃣ Variable Length Argument")
print("Method 1️⃣")


def add(a, *b):
    c = a
    for i in b:
        c += i
    print(c)


add(5, 5, 5, 5)

print("Method 2️⃣")


def add(*b):
    c = 0
    for i in b:
        c += i
    print(c)


add(5, 5, 5, 5)

print("Method 3️⃣")


def add(a, *b):
    c = a + sum(b)
    print(c)


add(5, 5, 5, 5)
print()

print("#️⃣ Keyword Variable Length Arguments | kwargs")
print("Method 1️⃣")


def person(name, **data):
    print(name)
    print(data)


person("navin", age=28, city="Mumbai", no=12345678)
print()

print("Method 2️⃣")


def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person("navin", age=28, city="Mumbai", no=12345678)
print()

print("#️⃣ Global vs Local Variable | Scope")

a = 10


def something():
    a = 15
    print("Local Variable / inside_function a=", a)


something()
print("Global Variable / outside_function a=", a)
print()

print("#️⃣ Not mentioning the Local Variable in a function")
a = 10


def something():
    print("Local Variable / inside_function a=", a)


something()
print("Global Variable / outside_function a=", a)
print()

print("#️⃣ Changing global variable when inside a function")
a = 10


def something():
    global a
    a = 15
    print("Local Variable / inside_function a=", a)


something()
print("Global Variable / outside_function a=", a)
print()

print("#️⃣ Using global and local variable inside a function")
a = 10
print(id(a))


def something():
    a = 9
    x = globals()['a']  # Not Necessary
    print(id(x))  # Address is same as global a because global a is not changed yet(next step)

    globals()['a'] = 20
    print("Local Variable / inside_function a=", a)


something()
print("Global Variable / outside_function a=", a)
print()

print("#️⃣ Find number of Even & Odd numbers from a list using function")

List = []
length_of_list = int(input("Enter length of the list: "))
for i in range(length_of_list):
    k = int(input("Enter the next integer: "))
    List.append(k)
print(List)


def even_odd(x):
    even = 0
    odd = 0
    for i in x:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("No. of even no's:", even)
    print("No. of odd no's:", odd)


even_odd(List)
print()

print("#️⃣ Another way to write the code")


def even_odd(x):
    even = 0
    odd = 0
    for i in x:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


even, odd = even_odd(List)

print("Even : {} and Odd : {}".format(even, odd))
print("Even : {} , Odd : {}".format(even, odd))
print("No. of even no's: {} and No. of odd no's: {}".format(even, odd))
print("No. of even no's: {} , No. of odd no's: {}".format(even, odd))
print()

print("#️⃣ Assignment Question")
print("#️⃣ Take 8 names from the user. Count and display the names having length more than 5 letters")
print()

names = []
long_names = []
for j in range(8):
    g = input("Enter the next name: ")
    names.append(g)
print(names)
print()


def filter_long_names(x):
    no_of_long_names = 0
    for t in x:
        if len(t) > 5:
            no_of_long_names += 1
            long_names.append(t)
        else:
            pass
    print("No of long names:", no_of_long_names)
    print("Long names are:", long_names)


filter_long_names(names)
print()
