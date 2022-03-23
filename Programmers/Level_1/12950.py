arr01 = [[1,2],[2,3]]
arr02 = [[3,4],[5,6]]
arr11 = [[1],[2]]
arr12 = [[3],[4]]

def solution(arr1, arr2):
    answer = []
    for p1,p2 in zip(arr1,arr2):
      inner=[]
      for i in range(len(p1)):
        inner.append(p1[i]+p2[i])
      answer.append(inner)
    return answer

print(solution(arr01, arr02))
print(solution(arr11, arr12))