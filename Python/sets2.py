n = int(input())
s = set(map(int, input().split()))
j = int(input())
k = set(map(int, input().split()))

symdiff = s.symmetric_difference(k)
unnn = set(symdiff)
for i in sorted(unnn):
    print(i)
