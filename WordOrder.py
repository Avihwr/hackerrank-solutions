import re
N = int(input())
lst = []
lst1 = []
c = 0
for y in range(N):
    word = input()
    lst.append(word)
    lst1.append(word)
for i in range(len(lst)):
    p = lst.count(lst[i])
    print(p)
    if p > 1:
        print("sad")
        for u in range(p-1):
            lst.remove(lst[i])
    #     print(len(lst1))
    # else:
    #     print(len(lst1))
for i in range(len(lst1)):
    x = lst1.count(lst1[i])
    print(x)





