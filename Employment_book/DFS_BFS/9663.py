for n in range(1, 15):
    answer = 0

    col = [False] * n
    right_d = [False] * n * 2
    left_d = [False] * n * 2


    def backtracking(row):
        global answer

        if row == n:
            answer += 1
            return

        for j in range(n if row else n // 2):
            if not col[j] and not right_d[row - j] and not left_d[row + j]:
                col[j] = True
                right_d[row - j] = True
                left_d[row + j] = True

                backtracking(row + 1)

                col[j] = False
                right_d[row - j] = False
                left_d[row + j] = False


    if n % 2:
        backtracking(0)
        answer *= 2

        j = n // 2
        col[j] = right_d[-j] = left_d[j] = True

        backtracking(1)

        print(answer)

    else:
        backtracking(0)
        print(answer * 2)


# 미리 n이 1 ~ 14일 때의 배열에 대한 N-Queen 결과 값 지정
def pre_setting(n):
    arr = [1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
    return arr[n - 1]
