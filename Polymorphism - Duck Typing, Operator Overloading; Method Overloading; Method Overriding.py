
print("#️⃣#️⃣ Duck Typing \n")

class ide_PyCharm:

    def execute(self):
        print("ide_PyCharm class function: 'execute'")

class ide_Mine:

    def execute(self):
        print("ide_Mine class function: 'execute'")

class Laptop:

    def code(self, ide):
        ide.execute(self)   # execute method can be referred to any class having execute method
                            # This is known as Duck Typing

lap1 = Laptop()

lap1.code(ide_PyCharm)      # Can change IDE call command here
print()
lap1.code(ide_Mine)      # Can change IDE call command here
print()

print("---------------------------------------")
print("#️⃣#️⃣ Polymorphism: Operator Overloading \n")

a = 6
b = 7

print(a+b, "\n")

print(int.__add__(a, b), "\n")

c = "6"
d = "7"

print(str.__add__(c, d), "\n")

print("#️⃣ Adding & comparing values of two objects in a class")
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        newm1 = self.m1 + other.m1
        newm2 = self.m2 + other.m2
        student3 = Student(newm1, newm2)

        return student3

    def __gt__(self, other):
        total_of_student1 = self.m1 + self.m2
        total_of_student2 = other.m1 + other.m2
        if total_of_student1 > total_of_student2:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.m1, self.m2)


student1 = Student(40, 20)
student2 = Student(50, 30)

student3 = student1 + student2

print(student3.m1, "\n")

if student1 > student2:
    print("Student1 scored more")
else:
    print("student2 scored more", "\n")

print("#️⃣ Printing value instead of address when calling an object")

x = 2
print(x.__str__())

print(student3)
print()

print("------------------------")
print("#️⃣#️⃣ Method Overloading \n")

class Shishye:

    def sum(self, p=None, q=None, r=None):
        if p != None and q != None and r != None:
            n = p+q+r
        elif p != None and q != None and r == None:
            n = p+q
        else:
            n = p
        return n

    def __add__(self, a, b):
        s = a + b
        return s


shishye1 = Shishye()

print(shishye1.__add__(60, 20))
print(shishye1.sum(10, 20))
print()

print("------------------------")
print("#️⃣#️⃣ Method Overriding \n")

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

a1 = B()    # child class' method (if exists) overrides super class' method
a1.show()
