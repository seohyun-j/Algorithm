n, L = map(int, input().split())
chk = [False] * 1001
for i in map(int, input().split()):
    chk[i] = True

answer = 0
distance = 0
while distance <= 1000:
    if chk[distance]:
        answer += 1
        distance += L
    else:
        distance += 1

print(answer)