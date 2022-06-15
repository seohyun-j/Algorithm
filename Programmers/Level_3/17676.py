l0 = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
l1 = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
l2 = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
      "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
      "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
      "2016-09-15 21:00:02.066 2.62s"]


def solution(lines):
    answer = 0
    arr = []
    for i in lines:
        day, time, plus_second = i.split()
        h, m, s = time.split(':')
        end = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000
        start = end - float(plus_second.replace('s', '')) * 1000 + 1
        arr.append([start, end])

    for a in arr:
        answer = max(answer, find(arr, a[0], a[0] + 1000), find(arr, a[1], a[1] + 1000))
    return answer


def find(log, st, en):
    cnt = 0
    for i in log:
        if i[0] < en and i[1] >= st:
            cnt += 1
    return cnt


print(solution(l0))
print(solution(l1))
print(solution(l2))
