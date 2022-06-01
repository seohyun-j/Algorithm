m0 = "ABCDEFG"
m1 = "CC#BCC#BCC#BCC#B"
m2 = "ABC"
info0 = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
info1 = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
info2 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]


def m_replace(s):
    if 'A#' in s:
        s = s.replace('A#', 'a')
    if 'C#' in s:
        s = s.replace('C#', 'c')
    if 'D#' in s:
        s = s.replace('D#', 'd')
    if 'F#' in s:
        s = s.replace('F#', 'f')
    if 'G#' in s:
        s = s.replace('G#', 'g')
    return s


def solution(m, musicinfos):
    answer = []
    m = m_replace(m)
    for idx, i in enumerate(musicinfos):
        st_t, en_t, title, music = i.split(',')
        st_t = st_t.split(':')
        en_t = en_t.split(':')
        time = int(en_t[1]) - int(st_t[1]) + (int(en_t[0]) - int(st_t[0])) * 60

        music = m_replace(music)
        music = music * (time // len(music)) + music[:time % len(music)]

        if m in music:
            answer.append([time, idx, title])

    if not answer:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2]


print(solution(m0, info0))
print(solution(m1, info1))
print(solution(m2, info2))