n = int(input())
s = set(map(int, input().split()))
j = int(input())
k = set(map(int, input().split()))

symdiff = s.symmetric_difference(k)
unn = set(symdiff)
print(len(unn))
