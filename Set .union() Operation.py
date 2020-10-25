n = int(input())
s = set(map(int, input().split()))
j = int(input())
k = set(map(int, input().split()))

unn = s.union(k)
unn = set(unn)
print(len(unn))
