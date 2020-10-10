if __name__ == '__main__':
    lst = []
    N = int(input())
    for _ in range(N):
        name, *line = input().split()
        if name == 'append':
            for i in line:
                lst.append(int(i))
        if name == 'insert':
            lst.insert(int(line[0]), int(line[1]))
        if name == 'print':
            print(lst)
        if name == 'remove':
            lst.remove(int(line[0]))
        if name == 'sort':
            lst.sort()
        if name == 'pop':
            lst.pop()
        if name == 'reverse':
            lst.reverse()
