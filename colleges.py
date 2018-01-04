#!/usr/bin/env python3
# -*- coding: utf-8 -*-

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats():
    enrollment = []
    tuition = []
    for school in universities:
        enrollment.append(school[1])
        tuition.append(school[2])

    enrollment.sort()
    tuition.sort()

    enrollment_mean = sum(enrollment)/len(enrollment)
    enrollment_median = enrollment[int(len(enrollment)/2)]

    tuition_mean = sum(tuition)/len(tuition)
    tuition_median = tuition[int(len(tuition)/2)]

    print("*"*20)
    print("Total students:", sum(enrollment))
    print("Total tuition:", sum(tuition))

    print("Student mean:", int(enrollment_mean))
    print("Student median:", enrollment_median)

    print("Tuition mean:", int(tuition_mean))
    print("Tuition median:", tuition_median)
    print("*"*20)


enrollment_stats()
