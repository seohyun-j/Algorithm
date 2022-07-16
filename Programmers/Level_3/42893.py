import re


def solution(word, pages):
    answer = []
    dic = {}
    homepage = {}
    extra = {}
    for j, i in enumerate(pages):
        cnt = re.sub("([^a-zA-z0-9]+)", " ", i)
        cnt = re.sub("([0-9]+)", " ", cnt).lower()
        cnt = cnt.split(' ')
        base = 0
        for k in cnt:
            if k == word.lower():
                base += 1
        dic[j] = [base, i.count('<a href=')]
        answer.append(base)

        idx = i.index('<meta property="og:url" content="') + len('<meta property="og:url" content="')
        en_idx = i[idx:].index('"') + idx
        tmp = i[idx:en_idx]
        homepage[tmp] = j

        key = i.count('<a href=')
        extra[j] = []
        for k in range(key):
            st = i.index('<a href="') + len('<a href="')
            en = i[st:].index('"') + st
            tmp = i[st:en]
            i = i[en:]
            extra[j].append(tmp)

    for i in range(len(pages)):
        base, plus = dic[i]
        for j in extra[i]:
            if j in homepage.keys():
                idx = homepage[j]
                answer[idx] += (base/plus)

    return answer.index(max(answer))


w0 = "blind"
w1 = "Muzi"
p0 = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
p1 = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]

print(solution(w0, p0))
print(solution(w1, p1))
