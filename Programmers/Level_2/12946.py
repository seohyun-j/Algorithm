def solution(n):
    answer = []

    def hanoi(n, start, end, assist):
        if n == 1:
            answer.append([start, end])
            return
        hanoi(n - 1, start, assist, end)  # n-1개 보조기둥으로 이동
        answer.append([start, end])  # 가장 큰 원판 결과기둥으로 이동
        hanoi(n - 1, assist, end, start)  # n-1개 보조기둥에서 결과 기둥으로 이동

    hanoi(n, 1, 3, 2)

    return answer


for i in range(2, 5):
    print(solution(i))
