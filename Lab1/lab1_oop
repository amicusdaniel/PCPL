import math

class Coef:
    def my_input(x, str):
        while True:
            print("Введите коэффициент  " + str + ": ")
            x = input()
            try:
                return float(x)
            except:
                print("Ошибка. Введите число")

    def __init__(self):
        self.a = self.my_input('A')
        self.b = self.my_input('B')
        self.c = self.my_input('C')


class Roots(Coef):

    def get_roots(self):
        D = (self.b) ** 2 - 4 * (self.a) * (self.c)

        self.x1 = ''
        self.x2 = ''

        if (D > 0):
            self.x1 = (-self.b - math.sqrt(D)) / (2 * self.a)
            self.x2 = (-self.b + math.sqrt(D)) / (2 * self.a)
        elif (D == 0):
            self.x1 = self.b / (-2 * self.a)
        else:
            print('Нет действительных корней')
        print(self.x1, self.x2)


if __name__ == "__main__":
    a = (Roots())
    a.get_roots()
