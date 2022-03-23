s0 = ["sun", "bed", "car"]
s1 = ["abce", "abcd", "cdx"]
n0 = 1
n1 = 2

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])

print(solution(s0,n0))
print(solution(s1,n1))