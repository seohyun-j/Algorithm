m0 = "ABCDEFG"
m1 = "CC#BCC#BCC#BCC#B"
m2 = "ABC"
info0 = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
info1 = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
info2 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]


def m_replace(s):
    large_s = ['A#', 'C#', 'D#', 'F#', 'G#']
    small_s = ['a', 'c', 'd', 'f', 'g']
    for p1, p2 in zip(large_s, small_s):
        if p1 in s:
            s = s.replace(p1, p2)
    return s


def solution(m, musicinfos):
    answer = []
    m = m_replace(m)
    for idx, val in enumerate(musicinfos):
        st_t, en_t, title, music = val.split(',')
        st_t = list(map(int, st_t.split(':')))
        en_t = list(map(int, en_t.split(':')))

        time = en_t[1] - st_t[1] + (en_t[0] - st_t[0]) * 60

        music = m_replace(music)
        music = music * (time // len(music)) + music[:time % len(music)]

        if m in music:
            answer.append([time, idx, title])

    answer = sorted(answer, key=lambda x: (-x[0], x[1]))
    if not answer:
        return "(None)"
    else:
        return answer[0][2]


print(solution(m0, info0))
print(solution(m1, info1))
print(solution(m2, info2))
