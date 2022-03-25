s0 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s1 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s2 = "{{20,111},{111}}"
s3 = "{{123}}"
s4 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

import re


def solution(s):
    answer = []
    s = s[2:-2].split(',{')
    s.sort(key=len)
    for i in s:
        numbers = re.findall("\d+", i)
        for j in numbers:
            if j.isdigit() and int(j) not in answer:
                answer.append(int(j))
    return answer


# 다른 사람 풀이 : Counter와 list map을 이용하여 구현 -> 훨씬 시간 단축됨
from collections import Counter


def other_solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


print(solution(s0))
print(solution(s1))
print(solution(s2))
print(solution(s3))
print(solution(s4))
