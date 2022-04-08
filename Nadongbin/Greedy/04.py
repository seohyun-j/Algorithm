n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0
member = 0

for x in data:
    member += 1
    if member >= x:
        group += 1
        member = 0

print(group)