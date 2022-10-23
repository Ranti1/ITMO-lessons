def summ_args(*args):
    suma = 0
    for ch in args:
        if type(ch) == int:
            suma += ch
        else:
            print(f"Error: bad type of variable {ch} - {type(ch)}, not 'int'")
            break
    print(f"Sum of the variables is {suma}")


summ_args(1, 3, 4, 131)
summ_args("1", 3, 13, 131, "3113")


def check_stroka(stroka):
    slovo = ""
    for i in range(len(stroka)):
        word = stroka[-i - 1]
        slovo += word
    if stroka == slovo:
        print(f"Слово {stroka} является палиндромом.")
    else:
        print(f"Слово {stroka} НЕ является палиндромом.")


check_stroka("казак")
check_stroka("холод")


def del_less_spaces(text):
    print(" ".join(text.split()))


del_less_spaces("Hi! My      name    is ...   ")
