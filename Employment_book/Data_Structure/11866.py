n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
idx = 0
answer = []
for _ in range(n):
    idx += k - 1
    idx %= len(arr)
    answer.append(arr.pop(idx))

print(f"<{', '.join(map(str, answer))}>")