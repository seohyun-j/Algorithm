l0 = 13
l1 = 24
r0 = 17
r1 = 27


# 내 풀이 -> 나머지 이용하여 계산 (이중 For문)
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        key = 0
        for j in range(1, i + 1):
            if i % j == 0:
                key += 1
        if key % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


# 다른 사람 풀이 -> 제곱수 이용 (제곱수는 약수의 개수가 홀수)
# 시간 절약 측면에서 위에 내가 구현한 것보다 훨씬 절약됨
def other_solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer


print(solution(l0, r0))
print(solution(l1, r1))
print(other_solution(l0, r0))
print(other_solution(l1, r1))