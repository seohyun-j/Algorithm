arr0 = [1,1,3,3,0,1,1]
arr1 = [4,4,4,3,3]

def solution(arr):
  return [num for i, num in enumerate(arr) if arr[i]!=arr[i-1] or i==0]

print(solution(arr0))
print(solution(arr1))