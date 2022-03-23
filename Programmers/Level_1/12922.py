n0 = 3
n1 = 4

def solution(n):
    return '수박'*(n//2) if n%2==0 else '수박'*(n//2)+'수'

# 위는 내가 진행한 풀이로 if문을 위에 쓰고 return 하는 것보다 한줄로 표현하는 것이 빠름
# 아래는 다른 사람의 풀이로 배열을 이용한 것으로 느리지만 직관적

def other_solution(n):
    s = '수박' * n
    return s[:n]

print('------ME------')
print(solution(n0))
print(solution(n1))

print('\n----OTHER-----')
print(other_solution(n0))
print(other_solution(n1))