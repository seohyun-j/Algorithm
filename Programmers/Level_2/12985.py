N = 8
A = 4
B = 7


# 이 문제는 접근하다가 포기하였는데, 접근을 2로 나누어 몫을 이용하는 방법과 비트 연산자를 이용하는 방법이 존재하였다.
# 속도 측면에서 other_solution이 훨씬 빠르다.
def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a + 1) // 2, (b + 1) // 2
    return answer


def other_solution(n, a, b):
    answer = 0
    arr = [i for i in range(1, n + 1)]
    if a > b:
        a, b = b, a

    while True:
        divide = []
        answer += 1
        l = len(arr)
        for i in range(0, len(arr), 2):
            confirm = arr[i:i + 2]
            if confirm == [a, b]:
                break
            if a in confirm:
                divide.append(a)
            elif b in confirm:
                divide.append(b)
            else:
                divide.append(confirm[0])
        arr = divide
        if len(arr) != l // 2:
            break

    return answer


print(solution(N, A, B))
print(other_solution(N, A, B))
