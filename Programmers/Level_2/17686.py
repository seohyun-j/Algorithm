f0 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
f1 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

import re


def solution(files):
    answer = [re.split(r"(\d+)", s) for s in files]
    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]


print(solution(f0))
print(solution(f1))
