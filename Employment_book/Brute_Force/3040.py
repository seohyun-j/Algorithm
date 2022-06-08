from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(input()))

arr = list(combinations(arr, 7))
for i in arr:
    if sum(i) == 100:
        print(*i, sep='\n')
