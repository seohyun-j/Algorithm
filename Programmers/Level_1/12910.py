arr0 = [5, 9, 7, 10]
arr1 = [2, 36, 1, 3]
arr2 = [3, 2, 6]
d0 = 5
d1 = 1
d2 = 10


def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    return [-1] if len(answer) == 0 else sorted(answer)
    # return sorted([n for n in arr if n%divisor == 0]) or [-1]
    # 위와 같이 or을 이용하여 풀이할 수도 있음


print(solution(arr0, d0))
print(solution(arr1, d1))
print(solution(arr2, d2))
