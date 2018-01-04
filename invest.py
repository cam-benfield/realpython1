#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def invest(amount, rate, time):
    amount = int(amount)
    rate = float(rate)
    time = int(time)
    year = 1
    print("Principal amount: $", amount)
    print("annual rate of return:", rate)
    while year <= time:
        amount = amount * (1 + rate)
        print("Year", year, ": $", amount)
        year += 1
    print()


invest(100, .05, 8)
invest(2000, .025, 5)
