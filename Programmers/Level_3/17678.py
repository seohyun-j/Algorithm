from collections import deque


def solution(n, t, m, timetable):
    answer = ''
    st_h = 9
    st_m = 0
    bus = [(st_h, st_m)]
    for i in range(n - 1):
        st_m += t
        if st_m >= 60:
            st_m -= 60
            st_h += 1
        bus.append((st_h, st_m))

    timetable = [tuple(map(int, i.split(':'))) for i in timetable]
    timetable.sort(key=lambda x: (x[0], x[1]))

    for i in range(n):
        cnt = 0
        print(bus[i], timetable)
        for j in timetable:
            print(timetable)
            if bus[i][0] > j[0]:
                cnt += 1
                lh, lm = timetable.pop(0)
            elif bus[i][0] == j[0]:
                if bus[i][1] >= j[1]:
                    cnt += 1
                    lh, lm = timetable.pop(0)

        if i == n - 1:
            if cnt < m:
                print(cnt)
                return str(bus[i][0]) + ':' + str(bus[i][1])
            else:
                return str(lh) + ':' + str(lm - 1)


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
