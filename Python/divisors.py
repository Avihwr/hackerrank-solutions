
def print_factors(x):
    lst = []
    for i in range(1, x + 1):
        if x % i == 0:
            lst.append(i)
    lst.remove(x)
    return lst


N = int(input())
lst1 = []
for _ in range(N):
    h = int(input())
    lst1.append(h)

for u in lst1:
    x = print_factors(u)
    if u == sum(x):
        print('YES')
    else:
        print('NO')
