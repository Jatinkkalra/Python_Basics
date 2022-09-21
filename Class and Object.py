
print("#️⃣#️⃣ Class and Object Basics \n")


class Computer:

    def config(self):
        print("i5, 16gb, 1TB")


a = 6
print(type(a), "\n")

comp1 = Computer
print(type(comp1), "\n")

comp1 = Computer()
print(type(comp1), "\n")

comp2 = Computer()

print("#️⃣ Calling a function inside the class Computer\n"
      "using comp1 and comp2 as objects / variables")
Computer.config(self=comp1)
Computer.config(comp2)
print()

print("#️⃣ Other way to call a class function")
comp1.config()
comp2.config()
print()

print("-----------------------")

print("#️⃣#️⃣ __init__ method\n")
print("Method 1️⃣: Assigning attributes inside configs function\n")


class Laptop:

    def configs(self, position, cpu, ram):
        self.position = position
        self.cpu = cpu
        self.ram = ram
        print(position, cpu, ram)


laptop1 = Laptop()
laptop2 = Laptop()

laptop1.configs("Values inside configs: ", "i3", "4 gb")
laptop2.configs("Values inside configs: ", "Ryzen 3", "8 gb")
print()

print("Method 2️⃣: Assigning attributes inside __init__\n")


class Tablet:

    def __init__(self, position, cpu, ram):
        self.position = position
        self.cpu = cpu
        self.ram = ram
        print("init always gets executed")

    def configuration(self):
        print(self.position, self.cpu, self.ram)


Tablet1 = Tablet("Values inside __init__: ", "i5", "12 gb")
Tablet2 = Tablet("Values inside __init__: ", "Ryzen 5", "26 gb")

Tablet1.configuration()
Tablet2.configuration()
print()

print("#️⃣ Fetching & printing attribute values directly \n")

print("cpu of laptop1 is: ", laptop1.cpu)
print("ram of Tablet2 is: ", Tablet2.ram)
print()

print("---------------------------------------------")
print("#️⃣  Constructor, Self and Comparing Objects \n")


class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 18


c1 = Computer()
c2 = Computer()

print("#️⃣ Changing __init__ value."
      "Note: __init__ can be looked as\n"
      "a place to write in-built functions of the new class")

c1.age = 30

print(c1.name, c1.age)
print(c2.name, c2.age)
print()

print("#️⃣ Methods preferred over __init__ / in-built attributes in a new class")


class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 18

    def change(self):
        self.age = 60


c1 = Computer()
c2 = Computer()

c2.change()
print(c1.name, c1.age)
print(c2.name, c2.age)
print()

print("#️⃣ Compare Objects\n")
print("#️⃣ Comparing age of c1 and c2")
print("Method 1️⃣")


class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 18


c1 = Computer()
c2 = Computer()

if c1.age == c2.age:
    print("They are same", "\n")

print("Method 2️⃣")


class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 18

    def compare(self, other):
        if self.age == other.age:
            print("They are same")
        else:
            print("They are different")


c1 = Computer()
c2 = Computer()

c1.compare(c2)
print()

print("#️⃣ Another way to write")


class Computer:

    def __init__(self):
        self.name = "Navin"
        self.age = 18

    def compare(self, other):
        if self.age == other.age:
            return True


c1 = Computer()
c2 = Computer()

c2.age = 20

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
