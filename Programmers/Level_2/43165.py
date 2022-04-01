n0 = [1, 1, 1, 1, 1]
n1 = [4, 1, 2, 1]
t0 = 3
t1 = 4

from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

def d_solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0, 0)
    return answer


print(solution(n0, t0))
print(solution(n1, t1))


# 이 문제에서는 bfs보다 dfs가 속도와 메모리 측면에서 효율적이다.