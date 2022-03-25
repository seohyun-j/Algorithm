b0 = 10
b1 = 8
b2 = 24
y0 = 2
y1 = 1
y2 = 24


def solution(brown, yellow):
    all = brown + yellow
    for i in range(1, all):
        if all % i == 0:
            w = all // i
            h = all // w
            if (w - 2) * (h - 2) == yellow:
                return [max(w, h), min(w, h)]


print(solution(b0, y0))
print(solution(b1, y1))
print(solution(b2, y2))
