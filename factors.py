#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def factors():
    numinput = int(input("Enter a positive integer:"))
    n = 1
    while n <= numinput:
        if numinput % n == 0:
            print(n, "is a divisor of", numinput)
        else:
            pass
        n += 1


factors()
