d0 = [1, 3, 2, 5, 4]
d1 = [2, 2, 3, 3]
b0 = 9
b1 = 10


def solution(d, budget):
    answer = 0
    count = 0
    d.sort()
    for i in d:
        answer += i
        if answer > budget:
            break
        else:
            count += 1
    return count


print(solution(d0, b0))
print(solution(d1, b1))
