n = input()
result = 0

for i in n:
    if i == '0' or result == 0:
        result += int(i)
    else:
        result *= int(i)

print(result)