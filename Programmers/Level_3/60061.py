def check(ans):
    for x, y, val in ans:
        if val == 0:
            if y == 0 or [x - 1, y, 1] in ans or [x, y, 1] in ans or [x, y - 1, 0] in ans:
                continue
            else:
                return True
        else:
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans or ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans):
                continue
            else:
                return True
    return False


def solution(n, build_frame):
    answer = []

    for i in build_frame:
        x, y, val, how = i

        if how == 1:
            answer.append([x, y, val])
            if check(answer):
                answer.remove([x, y, val])
        else:
            answer.remove([x, y, val])
            if check(answer):
                answer.append([x, y, val])
                
    answer.sort()
    return answer


# x, y, a, b = 좌표, a가 1이면 보이고 a가 0이면 기둥, b가 0이면 삭제이고 1이면 설치임

b0 = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
b1 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
      [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(5, b0))
print(solution(5, b1))
