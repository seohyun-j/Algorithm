arr0 = [4,3,2,1]
arr1 = [10]

def solution(arr):
    arr.remove(min(arr))
    return [-1] if len(arr)==0 else arr

print(solution(arr0))
print(solution(arr1))