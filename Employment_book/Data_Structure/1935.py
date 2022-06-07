n = int(input())
tmp = input()
num = []
arr = []
for _ in range(n):
    num.append(int(input()))

for i in tmp:
    if i.isalpha():
        arr.append(num[ord(i)-ord('A')])
    else:
        b = arr.pop()
        a = arr.pop()
        if i == '+':
            arr.append(a+b)
        elif i == '-':
            arr.append(a-b)
        elif i == '*':
            arr.append(a*b)
        else:
            arr.append(a/b)


print(f'{arr[0]:.2f}')
