#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def passwordcheck():
    pwrequest = "Tell me your password:"
    pwinput = input(pwrequest)
    if pwinput:
        first_letter = pwinput[0].upper()
        print("The first leter you entered was:", first_letter)
    else:
        passwordcheck()


passwordcheck()
