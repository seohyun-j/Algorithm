c0 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
c1 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]


def solution(clothes):
    result = 1
    closet = {}
    for i in clothes:
        key = i[1]
        val = i[0]
        if key in closet:
            closet[key].append(val)
        else:
            closet[key] = [val]

    for key in closet.keys():
        result = result * (len(closet[key]) + 1)

    return result - 1


print(solution(c0))
print(solution(c1))