n0 = 10
n1 = 5

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# 에라토스테네스의 체 이용하면 기존의 소수찾는 제곱근 알고리즘보다 빨라진다

print(solution(n0))
print(solution(n1))