people0 = [70, 50, 80, 50]
people1 = [70, 80, 50]
limit0 = 100

from collections import deque


def solution(people, limit):
    boat = 0
    people.sort()
    people = deque(people)
    while people:
        if len(people) >= 2:
            if people[0] + people[-1] <= limit:
                people.pop()
                people.popleft()
            else:
                people.pop()
        else:
            people.pop()
        boat += 1
    return boat


print(solution(people0, limit0))
print(solution(people1, limit0))
