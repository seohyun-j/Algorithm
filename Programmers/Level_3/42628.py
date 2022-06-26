import heapq


def solution(operations):
    operations = [i.split() for i in operations]
    arr = []
    for key, val in operations:
        if key == 'I':
            heapq.heappush(arr, int(val))
        elif arr:
            if val == '-1':
                heapq.heappop(arr)
            else:
                arr.pop(arr.index(max(arr)))
        else:
            continue
    return [heapq.nlargest(1, arr)[0], arr[0]] if arr else [0, 0]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
