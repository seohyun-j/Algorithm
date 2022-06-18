# 내가 풀이한 방법으로 시간초과에 걸림(완전탐색)
def solution(enroll, referral, seller, amount):
    dic = {i: 0 for i in enroll}
    for name, key in zip(seller, amount):
        idx = enroll.index(name)
        val = key * 10
        dic[name] += (key * 100 - val)

        if referral[idx] != '-':
            dic[referral[idx]] += val

        while referral[idx] != '-':
            name = referral[idx]
            idx = enroll.index(name)
            val = val // 10

            if val != 0:
                dic[name] -= val

                if referral[idx] != '-':
                    dic[referral[idx]] += val

    return list(dic.values())


# 남이 풀이한 방법으로 시간이 훨씬 단축됨(DP)
def other_solution(enroll, referral, seller, amount):
    n = len(enroll)
    dic = {val: idx + 1 for idx, val in enumerate(enroll)}
    parents = [0] * (n + 1)
    answer = [0] * (n + 1)

    for i in range(n):
        if referral[i] != '-':
            parents[i + 1] = dic[referral[i]]

    for i in range(len(seller)):
        match(parents, amount[i] * 100, dic[seller[i]], answer)

    return answer[1:]


def match(parents, money, num, answer):
    if parents[num] == num or money // 10 == 0:
        answer[num] += money
        return

    send = money // 10
    mine = money - send
    answer[num] += mine
    match(parents, send, parents[num], answer)
    return


e0 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
e1 = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
r0 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
r1 = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
s0 = ["young", "john", "tod", "emily", "mary"]
s1 = ["sam", "emily", "jaimie", "edward"]
a0 = [12, 4, 2, 5, 10]
a1 = [2, 3, 5, 4]

print(solution(e0, r0, s0, a0))
print(solution(e1, r1, s1, a1))

print(other_solution(e0, r0, s0, a0))
print(other_solution(e1, r1, s1, a1))
