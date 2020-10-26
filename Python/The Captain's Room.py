import math
from collections import Counter

K = int(input())
integers = list(map(int, input().split()))
length = len(integers)
s = set(integers)
groups = math.floor(length/K)

occ = Counter(integers)

for i, k in occ.items():
    if k == 1:
        print(i)
    else:
        continue


