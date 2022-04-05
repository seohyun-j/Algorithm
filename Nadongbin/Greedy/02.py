n, m = map(int, input().split())
min_arr = []

for i in range(n):
    data = list(map(int, input().split()))
    min_arr.append(min(data))

print(max(min_arr))
