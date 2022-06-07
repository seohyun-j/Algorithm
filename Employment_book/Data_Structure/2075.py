arr = []
n = int(input())

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.extend(tmp)

arr.sort()
print(arr[n-1])