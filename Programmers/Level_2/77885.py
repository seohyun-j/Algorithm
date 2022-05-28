numbers0 = [2, 7]


def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            num = list(bin(i)[2:])
            num[-1] = '1'
        else:
            num = "0" + bin(i)[2:]
            idx = num.rfind('0')
            num = list(num)
            num[idx] = '1'
            num[idx+1] = '0'

        answer.append(int(''.join(num),2))

    return answer


print(solution(numbers0))
