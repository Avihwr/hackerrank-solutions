def split_and_join(line):
    # write your code here
    a = line.split(" ")
    x = "-".join(a)
    print(x)


if __name__ == '__main__':
    line = str(input())
    split_and_join(line)
