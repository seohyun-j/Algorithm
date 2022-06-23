from collections import deque


def solution(n, t, m, timetable):
    answer = 0
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()
    bus = [9 * 60 + t * i for i in range(n)]

    idx = 0
    for key in bus:
        cnt = 0
        while cnt < m and idx < len(timetable) and timetable[idx] <= key:
            idx += 1
            cnt += 1

        if cnt < m:
            answer = key
        else:
            answer = timetable[idx - 1] - 1
    return str(answer // 60).zfill(2) + ':' + str(answer % 60).zfill(2)


arr0 = ["08:00", "08:01", "08:02", "08:03"]
arr1 = ["09:10", "09:09", "08:00"]
arr2 = ["09:00", "09:00", "09:00", "09:00"]
arr3 = ["00:01", "00:01", "00:01", "00:01", "00:01"]
arr4 = ["23:59"]
arr5 = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
        "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

print(solution(1, 1, 5, arr0))
print(solution(2, 10, 2, arr1))
print(solution(2, 1, 2, arr2))
print(solution(1, 1, 5, arr3))
print(solution(1, 1, 1, arr4))
print(solution(10, 60, 45, arr5))
