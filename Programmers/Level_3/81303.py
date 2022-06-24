N = 10 ** 9


class Node:
    survived = True

    def __init__(self, p, n):
        self.prev = p if p >= 0 else None
        self.next = n if n < N else None


def solution(n, k, cmd):
    global N
    N = n
    linked = {i: Node(i - 1, i + 1) for i in range(n)}
    idx = k
    removed = []

    for i in cmd:
        if i == 'C':
            linked[idx].survived = False
            removed.append(idx)

            prev, next = linked[idx].prev, linked[idx].next

            if prev is not None:
                linked[prev].next = linked[idx].next
            if next is not None:
                linked[next].prev = linked[idx].prev

            if linked[idx].next is None:
                idx = linked[idx].prev
            else:
                idx = linked[idx].next

        elif i == 'Z':
            recovered = removed.pop()
            linked[recovered].survived = True

            prev, next = linked[recovered].prev, linked[recovered].next

            if prev is not None:
                linked[prev].next = recovered
            if next is not None:
                linked[next].prev = recovered

        else:
            tmp, amount = i.split()

            if tmp == 'D':
                for _ in range(int(amount)):
                    idx = linked[idx].next
            elif tmp == 'U':
                for _ in range(int(amount)):
                    idx = linked[idx].prev

    return ''.join(["O" if linked[j].survived else "X" for j in range(n)])


c0 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
c1 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

print(solution(8, 2, c0))
print('-' * 50)
print(solution(8, 2, c1))
