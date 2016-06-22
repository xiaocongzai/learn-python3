# -*- coding:utf-8 -*-
import math


def quadraitc(a, b, c):
    # type: (int, int, int) -> object
    deta = b * b - 4 * a * c
    if deta < 0:
        print("无解")
    else:
        x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
        print("x1=%s,x2=%s" % (x1, x2))


quadraitc(1, 2, -3)
