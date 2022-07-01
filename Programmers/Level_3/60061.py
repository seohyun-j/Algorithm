def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b == 1:
            if a == 0:
                if y == 0:
                    answer.append([x, y, a])
                else:
                    tmp = [[x-1, y, 1], [x, y, 1], [x, y-1, 0]]
                    if tmp[0] in answer or tmp[1] in answer or tmp[2] in answer:
                        answer.append([x, y, a])
            else:
                tmp = [[x, y-1, 0], [x+1, y-1, 0], [x+1, y, 1], [x-1, y, 1]]
                if tmp[0] in answer or tmp[1] in answer or (tmp[2] in answer and tmp[3] in answer):
                    answer.append([x, y, a])
        else:
            if a == 0:
                if [x, y+1, 0] in answer:
                    if [x-1, y+1, 1] not in answer and [x, y+1, 1] not in answer:
                        continue
                if [x, y+1, 1] in answer:
                    if [x+1, y, 0] not in answer:
                        if [x+1, y+1, 1] not in answer or [x-1, y+1, 1] not in answer:
                            continue
                if [x-1, y+1, 1] in answer:
                    if [x, y+1, 1] not in answer or [x-2, y+1, 1] not in answer:
                        continue

                answer.pop(answer.index([x, y, a]))

            else:
                if [x, y, 0] in answer:
                    if [x, y-1, 0] not in answer and [x-1, y, 1] not in answer:
                        continue
                if [x+1, y, 0] in answer:
                    if [x+1, y-1, 0] not in answer and [x+1, y, 1] not in answer:
                        continue
                if [x-1, y, 1] in answer:
                    if [x-1, y-1, 0] not in answer and [x, y-1, 0] not in answer:
                        continue
                if [x+1, y, 1] in answer:
                    if [x+1, y-1, 0] not in answer and [x+2, y-1, 0] not in answer:
                        continue

                answer.pop(answer.index([x, y, a]))

    answer.sort(key = lambda x: (x[0], x[1], x[2]))
    return answer


# x, y, a, b = 좌표, a가 1이면 보이고 a가 0이면 기둥, b가 0이면 삭제이고 1이면 설치임

b0 = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
b1 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
      [1, 1, 1, 0], [2, 2, 0, 1]]

print(solution(5, b0))
print(solution(5, b1))
