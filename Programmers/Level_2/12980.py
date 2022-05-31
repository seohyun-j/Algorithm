num = [5, 6, 5000]


def solution(n):
    ans = 0
    while n > 0:
        ans += n % 2
        n //= 2
    return ans

# 2진수 이용하는 것이 훨씬 빠름
def bin_solution(n):
    return bin(n).count('1')


for i in num:
    print(solution(i))

print('-------- 2진수 이용 --------')
for i in num:
    print(bin_solution(i))
