e0 = "100-200*300-500+20"
e1 = "50*6-3*2"


def calc(op, eq, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if op[eq] == "*":
            split_data = exp.split('*')
            temp = []
            for s in split_data:
                temp.append(calc(op, eq + 1, s))
            return str(eval('*'.join(temp)))
        elif op[eq] == "+":
            split_data = exp.split('+')
            temp = []
            for s in split_data:
                temp.append(calc(op, eq + 1, s))
            return str(eval('+'.join(temp)))
        elif op[eq] == "-":
            split_data = exp.split('-')
            temp = []
            for s in split_data:
                temp.append(calc(op, eq + 1, s))
            return str(eval('-'.join(temp)))


from itertools import permutations


def solution(expression):
    answer = 0
    operations = list(permutations(['*', '-', '+'], 3))
    for op in operations:
        result = abs(int(calc(op, 0, expression)))
        if result > answer:
            answer = result
    return answer


print(solution(e0))
print(solution(e1))
