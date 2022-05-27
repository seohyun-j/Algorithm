n0 = "1924"
n1 = "1231234"
n2 = "4177252841"
k0 = 2
k1 = 3
k2 = 4

# 내가 푼 문제 풀이 방법 -> 정확성 테스트에서 시간초과로 걸림
from itertools import combinations


def solution(number, k):
    answer = 0
    cnt = list(combinations(range(len(number)), k))
    for i in cnt:
        tmp = ''
        for j in range(len(number)):
            if j not in i:
                tmp += number[j]
        answer = max(int(tmp), answer)
    return str(answer)


# 위의 식 간단화 하면 아래와 같이 되는데 이것도 시간초과
# 따라서 조합을 사용함에 있어 많은 시간이 발생하므로 조합 사용 X
def solution(number, k):
    cnt = list(combinations(list(number), len(number) - k))
    return ''.join(sorted(cnt, reverse=True)[0])


# stack의 LIFO 이용하고, k -= 1을 이용하여 진행함
# 시간 복잡도 O(n)
def solution(number, k):
    answer = []
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    return ''.join(answer[:len(answer)-k])


print(solution(n0, k0))
print(solution(n1, k1))
print(solution(n2, k2))
