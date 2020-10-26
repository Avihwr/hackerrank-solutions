#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    scoreA = 0
    scoreB = 0
    for i, j in zip(range(len(a)), range(len(b))):
        if a[i] > b[i]:
            scoreA += 1
        elif b[i] > a[i]:
            scoreB += 1
    return scoreA, scoreB



a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
lst = list(result)
for p in lst:
    print(p, end=' ')

