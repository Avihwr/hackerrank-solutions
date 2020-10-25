n = int(input())
s = set(map(int, input().split()))
j = int(input())
k = set(map(int, input().split()))

diff = s.difference(k)
unn = set(diff)
print(len(unn))
