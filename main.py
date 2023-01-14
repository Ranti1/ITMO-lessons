def repeat(func):
    def wrapper():
        for i in range(3):
            print(f"{i + 1}. {func()}")

    return wrapper()


def square(*args):
    try:
        summ = 0
        for num in args:
            summ += num ** 2
        return summ
    except TypeError:
        summ = 0
        for num in args:
            summ += int(num) ** 2
        return summ
    except ValueError:
        return TypeError()


print(square(1, "2", "3"))
