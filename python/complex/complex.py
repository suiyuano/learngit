# 复数运算

import math

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 加
    def add(self):
        return Number(self.x.r + self.y.r, self.x.im + self.y.im).show()

    # 减
    def sub(self):
        return Number(self.x.r - self.y.r, self.x.im - self.y.im).show()
    
    # 乘
    def multi(self):
        return Number(self.x.r * self.y.r - self.x.im * self.y.im, self.y.r * self.x.im + self.x.r * self.y.im).show()


class Number:

    def __init__(self, x, y):
        self.r = x
        self.im = y

    def show(self):
        print(self.r, self.im)



c1 = Number(2, 3)

c2 = Number(8, -1)

c = Complex(c1, c2)

c.add()

c.sub()

c.multi()






