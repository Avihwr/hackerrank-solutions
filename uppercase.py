#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    lst =[]
    x = s.split(" ")
    for i in range(len(x)):
        j = x[i].capitalize()
        lst.append(j)
    x = " ".join(lst)
    return x



if __name__ == '__main__':


    s = input()

    result = solve(s)

    print(result)