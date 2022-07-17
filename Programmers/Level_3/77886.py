import re


def solution(s):
    answer = []
    for i in s:
        cnt, idx, stack = 0, 0, ""
        while idx < len(i):  # 110 찾기
            idx = i.index('110')

    return answer


print(solution(["1110", "100111100", "0111111010"]))
