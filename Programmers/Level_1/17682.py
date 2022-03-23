n0 = '1S2D*3T'
n1 = '1D2S#10S'
n2 = '1D2S0T'
n3 = '1S*2T*3S'
n4 = '1D#2S*3S'
n5 = '1T2D3D#'
n6 = '1D2S3T*'


def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    sdt = ['S', 'D', 'T']
    for i in range(len(dartResult)):
      if dartResult[i] in sdt:
        if dartResult[i-1] == 'k':
          answer.append(10**(sdt.index(dartResult[i])+1))
        else:
          answer.append(int(dartResult[i-1])**(sdt.index(dartResult[i])+1))
      elif dartResult[i] == '*':
        answer[-1] = answer[-1]*2
      elif dartResult[i] == '*':
        answer[-1] = answer[-1]*(-1)
        print(answer[-1])
    print(answer)
    return sum(answer)




print(solution(n0))
print(solution(n1))
print(solution(n2))
print(solution(n3))
print(solution(n4))
print(solution(n5))
print(solution(n6))
