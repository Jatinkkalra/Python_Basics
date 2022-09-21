
print("#️⃣#️⃣ Iterator")

nums = [4, 5, 6, 9]

print(nums[3], "\n")

for i in nums:
    print(i, end=" ")
print()
print()

it = iter(nums)
print(it)
print(it.__next__())    # next can be written in two ways:
print(it.__next__())    # In-built function next and method next
print(it.__next__())
print()

print(next(it))     # next sequence doesn't break with method format
print()

print("#️⃣ Next method in a new class")

class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1   # val is not getting increased here.
            return val
        else:
            raise StopIteration   # break function doesn't work


values = TopTen()

print(next(values), "\n")

for i in values:
    print(i)        # next sequence continues
print()

print("--------------------------------")
print("#️⃣#️⃣ Generators \n")
print("#️⃣ First five numbers")
def first_five():

    yield 1     # return would lead to '1' being printed directly.
    yield 2
    yield 3
    yield 4
    yield 5

values = first_five()

print(values)
print(values.__next__())
print(values.__next__())
print(next(values))      # next sequence continues

for i in values:
    print(i)        # next sequence continues
print()

print("#️⃣ First 10 perfect squares")
def first_10_perfect_squares():
     for n in range(1, 11):
         perfect_square = n*n
         yield perfect_square   # print would have given the result directly

answer = first_10_perfect_squares()
print(answer)   # this won't work. Will need to use next or for loop.

for i in answer:
    print(i)

