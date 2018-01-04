#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random
import time

start_time = time.time()
probsdict = {
    "1": .87,
    "2": .65,
    "3": .17
}


def election(region):
    print("Region", region)
    cand_a_votes = 0
    cand_b_votes = 0
    for elections in range(0, 10000):
        if random() >= probsdict[region]:
            cand_a_votes += 1
        else:
            cand_b_votes += 1
    if cand_a_votes > cand_b_votes:
        print("Candidate A Wins!")
    elif cand_b_votes > cand_a_votes:
        print("Candidate B Wins!")
    else:
        print("No one wins this region!")


election("1")
election("2")
election("3")

print("--- %s seconds ---" % (time.time() - start_time))
