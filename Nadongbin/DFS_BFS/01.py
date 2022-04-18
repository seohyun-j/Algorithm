n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

answer = 0


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answer += 1

print(answer)
