s0 = "aabbaccc"
s1 = "ababcdcdababcdcd"
s2 = "abcabcdede"
s3 = "abcabcabcabcdededededede"
s4 = "xababcdcdababcdcd"


def solution(s):
    n = len(s)
    answer = n
    for unit in range(1, n // 2 + 1):
        cnt = 1
        now = s[:unit]
        tmp_answer = ''
        for i in range(unit, n + unit, unit):
            if s[i:i + unit] == now:
                cnt += 1
            else:
                if cnt > 1:
                    tmp_answer += str(cnt) + now
                else:
                    tmp_answer += now
                now = s[i:i + unit]
                cnt = 1
        answer = min(answer, len(tmp_answer))
    return answer


print(solution(s0))
print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
