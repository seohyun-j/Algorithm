b0 = 2
b1 = 100
b2 = 100
w0 = 10
w1 = 100
w2 = 100
t0 = [7, 4, 5, 6]
t1 = [10]
t2 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = deque([])
    time = deque([])
    truck_weights = deque(truck_weights)
    while truck_weights:

        if len(time) != 0:
            if answer == bridge_length + time[0]:
                que.popleft()
                time.popleft()

        if len(que) <= bridge_length and sum(que) + truck_weights[0] <= weight:
            que.append(truck_weights[0])
            time.append(answer)
            truck_weights.popleft()

        answer += 1

    return answer + bridge_length


print(solution(b0, w0, t0))
print(solution(b1, w1, t1))
print(solution(b2, w2, t2))