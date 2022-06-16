def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times)*n

    while left <= right:
        mid = (left + right) // 2
        checked = 0

        for t in times:
            checked += (mid // t)
            if checked > n:
                break

        if checked >= n:
            answer = mid
            right = mid - 1
        elif checked < n:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
