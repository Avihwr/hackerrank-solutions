# def average(array):
#     N = int(input())
#     array = set(map(int, input().split()))
#     avg = sum(set)/len(set)
#     return avg

def average(array):
    s = set(array)
    avg = sum(s)/len(s)
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)