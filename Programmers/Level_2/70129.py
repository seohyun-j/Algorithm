S = ["110010101001", "01110", "1111111"]


def solution(s):
    w_cnt, cnt = 0, 0
    while s != '1':
        tmp = ''
        w_cnt += 1
        for i in s:
            if i == '0':
                cnt += 1
                pass
            else:
                tmp += i
        s = bin(len(tmp))[2:]
    return [w_cnt, cnt]


def other_solution(s):
    w_cnt, cnt = 0, 0
    while s != '1':
        w_cnt += 1
        num = s.count('1')
        cnt += (len(s) - num)
        s = bin(num)[2:]
    return [w_cnt, cnt]


for i in S:
    print(solution(i))
    print(other_solution(i))
