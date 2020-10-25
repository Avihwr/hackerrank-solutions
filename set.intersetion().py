n = int(input())
s = set(map(int, input().split()))
j = int(input())
k = set(map(int, input().split()))

intskn = s.intersection(k)
unn = set(intskn)
print(len(unn))
