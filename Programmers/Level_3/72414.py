def to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time %= 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time %= 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


def to_int(time):
    time = time.split(':')
    time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    return time


def solution(play_time, adv_time, logs):
    play_time = to_int(play_time)
    adv_time = to_int(adv_time)

    dp = [0] * (play_time + 1)
    answer = 0
    most_view = 0

    if play_time == adv_time:
        return '00:00:00'

    for i in logs:
        st, en = i.split('-')
        st = to_int(st)
        en = to_int(en)
        dp[st] += 1
        dp[en] -= 1

    for i in range(1, play_time + 1):
        dp[i] = dp[i] + dp[i - 1]

    for i in range(1, play_time + 1):
        dp[i] = dp[i] + dp[i - 1]

    for i in range(adv_time - 1, play_time + 1):
        if i >= adv_time:
            if most_view < dp[i] - dp[i - adv_time]:
                most_view = dp[i] - dp[i - adv_time]
                answer = i - adv_time + 1
        else:
            if most_view < dp[i]:
                most_view = dp[i]
                answer = i - adv_time + 1

    return to_str(answer)


p0 = "02:03:55"
p1 = "99:59:59"
p2 = "50:00:00"
a0 = "00:14:15"
a1 = "25:00:00"
a2 = "50:00:00"
l0 = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
l1 = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
l2 = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(p0, a0, l0))
print(solution(p1, a1, l1))
print(solution(p2, a2, l2))
