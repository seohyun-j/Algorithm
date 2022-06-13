n, m = map(int, input().split())
arr = list(map(int, input().split()))

low = max(arr)
high = sum(arr)
mid = (low + high) // 2
answer = high


def parametric(x):
    cnt = 1
    blue = 0
    for i in arr:
        if blue + i <= x:
            blue += i
        else:
            cnt += 1
            blue = i

    return cnt <= m


while low <= high:
    if parametric(mid):
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

    mid = (low + high) // 2

print(answer)
