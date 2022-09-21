
def div(a, b):
    print(a/b)


print("#️⃣ Changing code of a function directly \n")


def division(a, b):
    if a < b:
        a, b = b, a
    print(a/b)


division(2, 4)
print()

print("#️⃣ Changing code of a function using decorators \n")


def smart_div(x):
    def updated(a, b):
        if a < b:
            a, b = b, a
        return x(a, b)
    return updated


div = smart_div(div)

div(2, 4)
print()

print("#️⃣ Special Variable: __name__ \n")

print(__name__, "\n")

# First create a final function calling all other executable codes of the module
# Then create the name = main func under an if statement and out the last function inside it
# This way the current module code will not be executed when imported in another module


def main():
    division(2, 4)
    div(2, 4)


if __name__ == "__main__":
    main()
