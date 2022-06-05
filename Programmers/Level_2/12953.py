arr0 = [2, 6, 8, 14]
arr1 = [1, 2, 3]

from math import gcd


def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = (answer * i) // gcd(answer, i)
    return answer


print(solution(arr0))
print(solution(arr1))
