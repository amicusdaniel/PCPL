import math


def my_input(a):
    print(a)

    while True:
        k = input()
        try:
            return float(k)

        except ValueError:
            print('Ошибка. Введите число')


def root(a, b, c):
    D = b ** 2 - 4 * a * c

    if (D == 0):
        x1 = (-b) / (2 * a)
        print(x1, x2)
    elif (D > 0):
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(x1)
    else:
        print('Нет действительных корней')


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    a = my_input('Введите коэффициент A: ')
    b = my_input('Введите коэффициент B: ')
    c = my_input('Введите коэффициент C: ')
    root(a, b, c)
