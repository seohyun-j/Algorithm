dic = {}
for i in range(int(input())):
    key = input()
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1

dic = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
print(dic[0][0])