
print("#️⃣ Inheritance: Single-Level Inheritance, Multi-Level Inheritance, Multiple Inheritance")
print("#️⃣ Super Class / Parent Class.  Sub Class / Child Class \n")

print("#️⃣#️⃣ Multi-level Inheritance")


class A:
    def feature1(self):
        print("Feature 1 is working")


class B(A):   # Child class or Sub class

    def feature2(self):
        print("Feature 2 is working")


class C(B):

    def feature3(self):
        print("Feature 3 is working")


print("#️⃣ Assigning class A and interacting afterwards")

a1 = A()

a1.feature1()
print()

print("#️⃣ Assigning class B and interacting afterwards")
b1 = B()

b1.feature1()
b1.feature2()
print()

print("#️⃣ Assigning class C and interacting afterwards")

c1 = C()

c1.feature3()
c1.feature2()
c1.feature1()
print()

print("#️⃣#️⃣ Multiple Inheritance")


class A:
    def feature1(self):
        print("Feature 1 is working")


class B:   # Child class or Sub class

    def feature2(self):
        print("Feature 2 is working")


class C(A, B):

    def feature3(self):
        print("Feature 3 is working")


print("#️⃣ Assigning class A and interacting afterwards")

a1 = A()

a1.feature1()
print()

print("#️⃣ Assigning class B and interacting afterwards")

b1 = B()

b1.feature2()
print()

print("#️⃣ Assigning class C and interacting afterwards")

c1 = C()

c1.feature3()
c1.feature2()
c1.feature1()
print()

print("--------------------------------")
print("#️⃣#️⃣ Constructor in Inheritance \n")


class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 is working")


class B(A):   # Child class or Sub class

    def feature2(self):
        print("Feature 2 is working")


print("#️⃣ Checking if constructor / init of A will be called")

b1 = B()
print()

print("#️⃣ Checking if constructor / init of A will be called when B has its own")


class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 is working")


class B(A):
    def __init__(self):
        print("in B init")

    def feature2(self):
        print("Feature 2 is working")


b2 = B()
print()

print("#️⃣#️⃣ Super Method(). Calling init of both classes")


class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 is working")


class B(A):   # Child class or Sub class
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature2(self):
        print("Feature 2 is working")


b3 = B()
print()

print("#️⃣#️⃣ Super() Method in Multiple Inheritance")
print("Note: Super method always prefer the left argument first \n"
"      Also known as Method Resolution Order (MRO)")


class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 of A is working")


class B:
    def __init__(self):
        print("in B init")

    def feature1(self):
        print("Feature 1 of B is working")


class C(A, B):   # Super() will prefer A, the left argument
    def __init__(self):
        super().__init__()
        print("in C init")

    def feature3(self):
        print("Feature 3 is working")
        super().feature1()  # Super() can be used to call any function


c1 = C()
c1.feature1()
print()

print("#️⃣ Using Super() to call a function")
c1.feature3()
