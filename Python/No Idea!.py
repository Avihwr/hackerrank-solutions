n, m = input().split()
integers = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for i in integers:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
    else:
        happiness += 0
print(happiness)