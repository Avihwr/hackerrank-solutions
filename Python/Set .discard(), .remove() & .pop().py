n = int(input())
s = set(map(int, input().split()))
J = int(input())
for _ in range(J):
    inp = input().split()
    if inp[0] == 'pop':
        s.pop()
    if inp[0] == 'remove':
        s.remove(int(inp[1]))
    if inp[0] == 'discard':
        s.discard(int(inp[1]))

print(sum(list(s)))

