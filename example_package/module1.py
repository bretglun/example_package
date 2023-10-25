from example_package import module2


def add(a, b):
    return a + b


print(f"Name: {__name__}")
print(f"Package: {__package__}")
print('This is imported module 1')
print(module2.introduce())