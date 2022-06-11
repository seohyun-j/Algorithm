from bisect import bisect_left, bisect_right


def bisect_func():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    m = int(input())
    com = list(map(int, input().split()))

    answer = []

    for i in com:
        answer.append(bisect_right(arr, i) - bisect_left(arr, i))

    return ' '.join(map(str, answer))


def dic_func():
    n = int(input())
    dic = {}

    for i in map(int, input().split()):
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    m = int(input())
    answer = []
    for j in map(int, input().split()):
        answer.append(dic[j] if j in dic else 0)

    return ' '.join(map(str, answer))


print(bisect_func())
print(dic_func())
