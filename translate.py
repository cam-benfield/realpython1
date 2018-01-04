#!/usr/bin/env python3
# -*- coding: utf-8 -*-

leetdict = {
    "a": "4",
    "b": "8",
    "e": "3",
    "l": "1",
    "o": "0",
    "s": "5",
    "t": "7"
}


def translate():
    translate_input = input("Enter some text:")
    for letter in leetdict:
        translate_input = translate_input.replace(letter, leetdict[letter])
    print(translate_input)


translate()
