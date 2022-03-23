n0 = 5
n1 = 6
arr01 = [9, 20, 28, 18, 11]
arr02 = [30, 1, 21, 17, 28]
arr11 = [46, 33, 33, 22, 31, 50]
arr12 = [27, 56, 19, 14, 14, 10]


def solution(n, arr1, arr2):
    answer = []
    arr1 = [bin(i)[2:].rjust(n, '0') for i in arr1]
    arr2 = [bin(i)[2:].rjust(n, '0') for i in arr2]
    key = ''
    for p1, p2 in zip(arr1, arr2):
        for k in range(n):
            if p1[k] == '0' and p2[k] == '0':
                key += ' '
            else:
                key += '#'
        answer.append(key)
        key = ''
    return answer


# 내 풀이는 arr1과 arr2를 따로 이진법으로 표시하여 rjust를 통해 오른쪽정렬해주었는데, 다른 풀이는 비트연산을 이용하여 나타내었다.
# 이는 훨씬 빨라지는 것을 확인할 수 있다.

def other_solution(n, arr1, arr2):
    answer = []
    for p1, p2 in zip(arr1, arr2):
        arr12 = str(bin(p1 | p2)[2:]).rjust(n, '0')
        arr12 = arr12.replace('1', '#')
        arr12 = arr12.replace('0', ' ')
        answer.append(arr12)
    return answer


print(solution(n0, arr01, arr02))
print(solution(n1, arr11, arr12))

print(other_solution(n0, arr01, arr02))
print(other_solution(n1, arr11, arr12))
