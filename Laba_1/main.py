#variant 17
# C2 = 17 % 2 = 1 | O1 = "-"
# C3 = 17 % 3 = 2 | C = C3 = 2
# C5 = 17 % 5 = 2 | O2 = %
# C7 = 17 % 7 = 3 | long - тип індексів i та j


class A:
    C = 2

    def __init__(self, a, n, b, m):
        self.S = 0
        if type(a) == int and type(n) == int and type(b) == int and type(m) == int:
            self.a = a
            self.n = n
            self.b = b
            self.m = m
        else:
            print('\033[31mERROR! a, n, b, m - целые числа!\033[0m')

    def calc(self):
        self.S = 0
        try:
            for i in range(self.a, self.n + 1):
                for j in range(self.b, self.m + 1):
                    self.S += (i % j) / (i - 2)
        except ZeroDivisionError:
            return '\033[31mERROR! Деление на ноль!\033[0m'
        except AttributeError:
            return '\033[31mERROR! У экземпляра нет атрибутов a, n, b, m!\033[0m'
        else:
            return self.S


a = A(1, 5, 1, 5)
print(a.calc())

b = A(0, 1, 1, 5)
print(b.calc())

c = A(-5, 0, -4, -1)
print(c.calc())

d = A(-5, 's', -4.2, -1.11)
print(d.calc())


