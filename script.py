# generator function
print("Generator function")
def square(n, limit = 10):
    for i in range(n):
        if i > limit:
            return
        yield i

for i in square(20, 15):
    print(i)


# generator expression
print("Generator expression")
square_gen = (i**2 for i in range(11))

for i in square_gen:
    print(i)


# generator with a custom iterator
print("Generator with a custom iterator")
class SquareCustomIterator:
    def __init__(self, start, end, step, limit = 100):
        self.pointer = 0
        self.array = [i for i in range(start, end, step)]
        self.limit = limit

    def __iter__(self): # returns self
        return self
    
    def __next__(self): # returns a single value or StopIteration
        if self.pointer >= len(self.array):
            raise StopIteration
        current_value = self.array[self.pointer]
        current_value_squared = current_value ** 2
        if current_value_squared > self.limit:
            raise StopIteration
        self.pointer += 1
        return current_value_squared
    
square_custom_iter = SquareCustomIterator(0, 15, 1, 150)

# using the iterator's __next__ method
while True:
    try:
        print(square_custom_iter.__next__())
    except StopIteration:
        break

print("Generator with a custom iterator using the iterator's __iter__ method")
square_custom_iter = SquareCustomIterator(0, 15, 1, 150)
# using the iterator's __iter__ method
for i in square_custom_iter:
    print(i)

