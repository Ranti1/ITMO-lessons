def repeat(func):
    def wrapper():
        for i in range(3):
            print(f"{i + 1}. {func()}")
    return wrapper()


@repeat
def square(*args):
    summ = 0
    for num in args:
        summ += num ** 2
    return summ


square(1, 2, 3)
