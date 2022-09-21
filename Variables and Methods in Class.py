
print("#️⃣ Types of Variables in Class \n")
print("#️⃣ Class Variables and Instance Variables")


class Cars:  # Below Area is called class namespace

    wheels = 4   # Class variables | Changes value for every object

    def __init__(self):  # Below Area is called instance namespace
        self.mil = 10   # Instance variable | Selected object values can be changed
        self.com = "BMW"   # Instance variable


c1 = Cars()
c2 = Cars()

c1.mil = 15

Cars.wheels = 5

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
print()

print("--------------------------------")
print("#️⃣ Types of Methods in Class")
print("#️⃣ Instance Methods: Accessors and Mutators, Class Methods and Static Methods\n")


class Student:

    school_name = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # Instance Method as self is used.
                    # Interacting with an object(student1) even though it's defined under class
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1  # Accessor. Fetching a value.

    def set_m1(self, value):
        self.m1 = value  # Mutator: Changing a value

    @classmethod
    def get_school_name(cls):
        return cls.school_name  # Class Method: Interacting with class variable

    @staticmethod
    def info():
        print("This is student class XI")  # Static Method.
                                            # Nothing to do with instance or class variable


student1 = Student(10, 20, 30)
student2 = Student(40, 50, 60)

print(student1.avg())
print(student2.avg())
print()

print("#️⃣ Accessor: Fetching a value.")
print(student1.get_m1(), "\n")

print("#️⃣ Accessor alternative. Using variable to fetch value.")
print(student1.m1, "\n")

print("#️⃣ Mutator: Changing a value")
student2.set_m1(55)
print(student2.m1, "\n")

print("#️⃣ Class Method: Interacting with class variable")
print(Student.get_school_name(), "\n")

print("#️⃣ Static Method: Nothing to do with instance or class variable")
Student.info()
