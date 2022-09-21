
print("#️⃣ Inner Class \n")


class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.laptop = self.Laptop()

    def show(self):
        print(student1.name, student1.roll_no)
        self.laptop.show()


    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


student1 = Student("Navin", 10)
student2 = Student("Reddy", 20)

print(student1, "\n")
print(student1.name, student1.roll_no, "\n")

student1.show()
print()

print("#️⃣ Calling an inner class attribute")
print(student1.laptop.brand, "\n")

laptop1 = Student.Laptop()
laptop2 = Student.Laptop()

print(laptop1)
print(laptop2)
print()

print(student1.show())




