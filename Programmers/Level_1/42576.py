p0 = ["leo", "kiki", "eden"]
p1 = ["marina", "josipa", "nikola", "vinko", "filipa"]
p2 = ["mislav", "stanko", "mislav", "ana"]
c0 = ["eden", "kiki"]
c1 = ["josipa", "filipa", "marina", "nikola"]
c2 = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    answer = []
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()


print(solution(p0, c0))
print(solution(p1, c1))
print(solution(p2, c2))
