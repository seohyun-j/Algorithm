n, m = map(int, input().split())
tree = list(map(int, input().split()))
low = 0
high = max(tree)
mid = (low + high) // 2


def parametric(m):
    cnt = 0
    for i in tree:
        if i > m:
            cnt += (i - m)

    return cnt


answer = 0
while low <= high:
    if parametric(mid) >= m:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

    mid = (low + high) // 2

print(answer)
