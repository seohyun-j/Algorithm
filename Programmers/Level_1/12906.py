arr0 = [1,1,3,3,0,1,1]
arr1 = [4,4,4,3,3]

def solution(arr):
  return [num for i, num in enumerate(arr) if arr[i]!=arr[i-1] or i==0]


# 두번째 내 풀이는 아래와 같은데 이게 효율성 테스트 면에서 훨 빠르다
def second_solution(arr):
  answer = []
  for i in arr:
    if not answer:
      answer.append(i)
    elif i != answer[-1]:
      answer.append(i)
  return answer


print(solution(arr0))
print(solution(arr1))