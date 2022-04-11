n, m = map(int, input().split())
arr = list(map(int, input().split()))

from itertools import combinations

comb = list(combinations(arr, 2))
cnt = 0

for i in comb:
    if len(set(i)) == 1:
        cnt += 1

print(len(comb)-cnt)