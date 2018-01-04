#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def exponent():
    userinput1 = float(input("Enter a base:"))
    userinput2 = float(input("Enter an exponent:"))
    expoutput = userinput1**userinput2
    print(userinput1, "to the power of", userinput2, "=", expoutput)


exponent()
