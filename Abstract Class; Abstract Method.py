
print("#️⃣#️⃣ Abstract Class and Abstract Method \n")

from abc import ABC, abstractmethod

class Computer(ABC):    # Abstract Class
    @abstractmethod
    def process(self):
        pass    # Abstract Method


# com = Computer()
# com.process()     # This execution will face an error

class Laptop(Computer):
    def process(self):
        print("Child Class of an abstract class")

com1 = Laptop()
com1.process()
