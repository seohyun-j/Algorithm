c0, c1, c2, c3, c4, c5 = 3, 3, 2, 5, 2, 0
city0 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
city1 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
city2 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
         "Rome"]
city3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
         "Rome"]
city4 = ["Jeju", "Pangyo", "NewYork", "newyork"]
city5 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]


def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in cities:
        i = i.lower()
        if cacheSize:
            if i not in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(i)
                answer += 5
            else:
                cache.pop(cache.index(i))
                cache.append(i)
                answer += 1
        else:
            answer += 5
    return answer


print(solution(c0, city0))
print(solution(c1, city1))
print(solution(c2, city2))
print(solution(c3, city3))
print(solution(c4, city4))
print(solution(c5, city5))
