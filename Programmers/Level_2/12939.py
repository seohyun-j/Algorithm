arr = ["1 2 3 4", "-1 -2 -3 -4", "-1 -1"]


def solution(s):
    s = [int(i) for i in s.split(' ')]
    return str(min(s)) + " " + str(max(s))


for x in arr:
    print(solution(x))
