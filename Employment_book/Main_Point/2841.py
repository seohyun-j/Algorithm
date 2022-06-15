import sys

input = sys.stdin.readline

n, p = map(int, input().split())
arr = [[] for _ in range(7)]
answer = 0

for _ in range(n):
    line, tmp = map(int, input().split())

    while arr[line] and arr[line][-1] > tmp:
        arr[line].pop()
        answer += 1

    if arr[line] and arr[line][-1] == tmp:
        continue

    arr[line].append(tmp)
    answer += 1

print(answer)
