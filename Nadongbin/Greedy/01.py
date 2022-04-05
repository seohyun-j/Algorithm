n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
key1 = m // k
key2 = m % k
max1 = arr[0]
max2 = arr[1]

answer = max1 * key1 * k + max2 * key2

print(answer)
