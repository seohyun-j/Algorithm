f0 = [180, 5000, 10, 600]
r0 = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
      "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
f1 = [120, 0, 60, 591]
r1 = ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
f2 = [1, 461, 1, 10]
r2 = ["00:00 1234 IN"]

import math


def solution(fees, records):
    answer = []
    base_time, base_fee, plus_time, plus_fee = fees
    dic = {}
    fee_dic = {}
    for i in records:
        time, num, chk = i.split(' ')
        if chk == 'IN':
            dic[num] = list(map(int, time.split(':')))
        else:
            h, s = list(map(int, time.split(':')))
            in_time = (h - dic[num][0]) * 60 + s - dic[num][1]
            del dic[num]

            if num in fee_dic:
                fee_dic[num] += in_time
            else:
                fee_dic[num] = in_time

    if len(dic) != 0:
        for num in dic:
            in_time = (23 - dic[num][0]) * 60 + 59 - dic[num][1]
            if num in fee_dic:
                fee_dic[num] += in_time
            else:
                fee_dic[num] = in_time

    fee_dic = sorted(fee_dic.items())

    for i in fee_dic:
        num, fee = i
        if fee <= base_time:
            answer.append(base_fee)
        else:
            result = base_fee + math.ceil((fee - base_time) / plus_time) * plus_fee
            answer.append(result)

    return answer


print(solution(f0, r0))
print(solution(f1, r1))
print(solution(f2, r2))
