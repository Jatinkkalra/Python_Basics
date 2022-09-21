
print("#️⃣#️⃣ Exception Handling: try, except and finally \n")

a = 5   # normal statement
b = 0   # normal statement

try:
    print("resource open")
    print(a/b)   # critical statement


except ZeroDivisionError as e:   # Can write any operation below
    print("Hey, you cannot divide by zero.", "Error:", e)   # e prints  the error message

except Exception as g:
    print("Something went wrong...", g)

finally:
    print("resource closed")

print("Bye", "\n")

try:
    print("resource open")
    k = int(input("Enter a number: "))
    print(k)

except ValueError as f:
    print("Input is not a number.", "Error:", f)
except Exception as g:
    print("Something went wrong...", "Error:", g)

finally:
    print("resource closed")
print()

print("----------------------------------")
print("#️⃣#️⃣ Multi-Threading \n")

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):  # run is an in-built method of Thread
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):  # run is an in-built method of Thread
        for i in range(5):
            print("Hi")
            sleep(1)

test_1 = Hello()
test_2 = Hi()

test_1.start()  # Executing start instead of run to call 2 different threads
sleep(0.2)
test_2.start()

test_1.join()
test_2.join()

print("Bye")
