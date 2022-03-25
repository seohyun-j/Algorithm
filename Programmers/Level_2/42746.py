n0 = [6, 10, 2]
n1 = [3, 30, 34, 5, 9]


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))


print(solution(n0))
print(solution(n1))