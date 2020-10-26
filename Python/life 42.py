lst = []
for _ in range(1, 1000):
    n = int(input())
    lst.append(n)
    if n == 42:
        break

lst.remove(42)
for u in lst:
    print(u)
