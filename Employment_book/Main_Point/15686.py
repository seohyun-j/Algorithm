from itertools import combinations

n, m = map(int, input().split())

houses = []
chickens = []

for i in range(n):
    for j, val in enumerate(map(int, input().split())):
        if val == 1:
            houses.append((i, j))
        if val == 2:
            chickens.append((i, j))


def find_distance(h, c):
    return abs(h[0] - c[0]) + abs(h[1] - c[1])


answer = 987654321

for comb in combinations(chickens, m):
    total = 0
    for h in houses:
        total += min(find_distance(h, c) for c in comb)

    answer = min(answer, total)

print(answer)
