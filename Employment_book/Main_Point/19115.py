n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
answer = 1

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            arr[i][j] = min(arr[i - 1][j - 1], arr[i - 1][j], arr[i][j - 1]) + 1
    answer = max(answer, max(arr[i]))

print(answer ** 2)
