#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def cointoss(trials):
    totalflips = 0
    for number in range(1, trials):
        init_flip = randint(0, 1)
        next_flip = init_flip
        flips = 0
        while next_flip == init_flip:
            next_flip = randint(0, 1)
            flips += 1
        totalflips = totalflips + flips
    print(totalflips/trials)


cointoss(10000)
