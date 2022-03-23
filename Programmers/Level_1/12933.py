n0 = 118372

def solution(n):
    answer = [i for i in str(n)]
    return int(''.join(sorted(answer,reverse=True)))

print(solution(n0))