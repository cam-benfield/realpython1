#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

worddict = {
    "nouns": ["fossil",
              "horse",
              "aardvark",
              "judge",
              "chef",
              "mango",
              "extrovert",
              "gorilla"
              ],
    "verbs": ["kicks",
              "jingles",
              "bounces",
              "slurps",
              "meows",
              "explodes",
              "curdles"
              ],
    "adjects": ["furry",
                "balding",
                "incredulous",
                "fragrant",
                "exuberant",
                "glistening"
                ],
    "prepos": ["against",
               "after",
               "into",
               "beneath",
               "upon",
               "for",
               "in",
               "like",
               "over",
               "within"
               ],
    "adverbs": ["curiously",
                "extravagantly",
                "tantalizingly",
                "furiously",
                "sensuously"
                ]
}

vowels = ['a', 'e', 'i', 'o', 'u']


def makePoem():
    adjective1 = random.choice(worddict["adjects"])
    adjective2 = random.choice(worddict["adjects"])
    adjective3 = random.choice(worddict["adjects"])
    while adjective1 == adjective2:
        adjective2 = random.choice(worddict["adjects"])
    while adjective3 == adjective1 or adjective3 == adjective2:
        adjective3 = random.choice(worddict["adjects"])
    noun1 = random.choice(worddict["nouns"])
    noun2 = random.choice(worddict["nouns"])
    noun3 = random.choice(worddict["nouns"])
    while noun1 == noun2:
        noun2 = random.choice(worddict["nouns"])
    while noun3 == noun1 or noun3 == noun2:
        noun3 = random.choice(worddict["nouns"])
    verb1 = random.choice(worddict["verbs"])
    verb2 = random.choice(worddict["verbs"])
    verb3 = random.choice(worddict["verbs"])
    while verb1 == verb2:
        verb2 = random.choice(worddict["verbs"])
    while verb3 == verb1 or verb3 == verb2:
        verb3 = random.choice(worddict["verbs"])
    adverb1 = random.choice(worddict["adverbs"])
    prepos1 = random.choice(worddict["prepos"])
    prepos2 = random.choice(worddict["prepos"])
    while prepos1 == prepos2:
        prepos2 = random.choice(worddict["prepos"])
    if adjective1[0] in vowels:
        art1 = "An"
    else:
        art1 = "A"
    if adjective2[0] in vowels:
        art2 = "an"
    else:
        art2 = "a"
    print("""%s %s %s

    %s %s %s %s %s the %s %s
    %s, the %s %s
    the %s %s %s %s %s %s
    """ % (art1, adjective1, noun1, art1, adjective1,
           noun1, verb1, prepos1, adjective2, noun2,
           adverb1, noun1, verb2, noun2, verb3, prepos2, art2,
           adjective3, noun3))


makePoem()
