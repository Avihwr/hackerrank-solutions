n = int(input())
s = set(map(int, input().split()))
J = int(input())
for _ in range(J):
    inp = input().split()
    if inp[0] == 'update':
        s1 = set(map(int, input().split()))
        s.update(s1)
    if inp[0] == 'intersection_update':
        s2 = set(map(int, input().split()))
        s.intersection_update(s2)
    if inp[0] == 'difference_update':
        s3 = set(map(int, input().split()))
        s.difference_update(s3)
    if inp[0] == 'symmetric_difference_update':
        s4 = set(map(int, input().split()))
        s.symmetric_difference_update(s4)

print(sum(list(s)))


