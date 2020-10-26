from collections import Counter

X = int(input())

size = Counter(input().split())

N = int(input())

amount = 0
for _ in range(N):
    shoe_size, xi = input().split()
    if shoe_size in size and size[shoe_size] > 0:
        size[shoe_size] -= 1
        amount = int(amount) + int(xi)
    else:
        pass
print(amount)
