name1 = "JEROEN"
name2 = "JAN"
name3 = "JAZ"


def solution(name):
    answer = 0
    idx = 0
    arr = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    while True:
        answer += arr[idx]
        arr[idx] = 0

        if sum(arr) == 0:
            break

        left, right = 1, 1
        while arr[idx - left] == 0:
            left += 1
        while arr[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right

    return answer


print(solution(name1))
print(solution(name2))
print(solution(name3))
