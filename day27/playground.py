def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 4, 5, 6))

def calculate(n, **kwargs):
    # for key, value in kwargs.items();
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


print(calculate(3, add=3, multiply = 5))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get("seats")

myCar = Car(make = "Nissan", model = "GTR",  color = 'red')
print(myCar.model)