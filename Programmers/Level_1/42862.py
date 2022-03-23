n0 = 5
n1 = 5
n2 = 3
l0 = [2, 4]
l1 = [2, 4]
l2 = [3]
r0 = [1, 3, 5]
r1 = [3]
r2 = [1]

def solution(n, lost, reserve):
    set_lost=set(lost)-set(reserve)
    set_reserve=set(reserve)-set(lost)
    for i in set_reserve:
      if i-1 in set_lost:
        set_lost.remove(i-1)
      elif i+1 in set_lost:
        set_lost.remove(i+1)
    return n - len(set_lost)

print(solution(n0,l0,r0))
print(solution(n1,l1,r1))
print(solution(n2,l2,r2))