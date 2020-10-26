N = input()

s = {'set'}
s.clear()
for _ in range(int(N)):
    name = input()
    s.add(name)
print(len(s))

