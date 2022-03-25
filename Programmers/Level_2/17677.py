str01 = 'FRANCE'
str02 = 'french'
str11 = 'handshake'
str12 = 'shake hands'
str21 = 'aa1+aa2'
str22 = 'AAAA12'
str31 = 'E=M*C^2'
str32 = 'e=m*c^2'

from collections import Counter


def solution(str1, str2):
    str1 = [str1[i:i + 2].upper() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2 = [str2[i:i + 2].upper() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    if len(str1) == 0 and len(str2) == 0:
        return 65536

    ct1 = Counter(str1)
    ct2 = Counter(str2)
    inter_ct = sum((ct1 & ct2).values())
    union_ct = sum((ct1 | ct2).values())
    return int(inter_ct / union_ct * 65536)


print(solution(str01, str02))
print(solution(str11, str12))
print(solution(str21, str22))
print(solution(str31, str32))