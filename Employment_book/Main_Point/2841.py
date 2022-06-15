n, p = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(arr)
tmp = []
chk = 0
answer = 0
for i in arr:
    idx, val = i
    tmp.sort()
    if chk != idx:
        chk = idx
        answer += len(tmp)
        if tmp:
            tmp = []
        else:
            tmp.append(val)
    else:
        if max(tmp) == val:
            continue
        elif max(tmp) < val:
            answer += 1
            tmp.append(val)
        else:
            while max(tmp) > val:
                answer += 1
                tmp.pop()
                print(tmp)

            answer += 1
            tmp.append(val)

print(answer)