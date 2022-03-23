n0 = "01033334444"
n1 = "027778888"

def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]

print(solution(n0))
print(solution(n1))