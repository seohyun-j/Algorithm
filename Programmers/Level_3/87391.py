def solution(n, m, x, y, queries):
    top = bottom = x
    left = right = y
    height, width = n - 1, m - 1

    for command, dx in queries[::-1]:
        # ← 이동
        if command == 0:
            if left != 0:
                left += dx
            right = min(width, right + dx)

        # → 이동
        elif command == 1:
            if right != width:
                right -= dx
            left = max(0, left - dx)

        # ↑ 이동
        elif command == 2:
            if top != 0:
                top += dx
            bottom = min(height, bottom + dx)

        # ↓ 이동
        else:
            if bottom != height:
                bottom -= dx
            top = max(0, top - dx)

        if left > right or top > bottom:
            return 0

    return (bottom - top + 1) * (right - left + 1)


q0 = [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]
q1 = [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]
q2 = [[2, 3], [3, 1], [0, 3]]
print(solution(2, 2, 0, 0, q0))
print(solution(2, 5, 0, 1, q1))
print(solution(3, 3, 1, 0, q2))
