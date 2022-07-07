# 크루스칼 알고리즘 이용
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]

    def find_parents(parent, n):
        if parent[n] != n:
            parent[n] = find_parents(parent, parent[n])
        return parent[n]

    def union_parent(parent, a, b):
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    for u, v, cost in costs:
        u = find_parents(parents, u)
        v = find_parents(parents, v)
        if u != v:
            union_parent(parents, u, v)
            answer += cost

    return answer


# set을 이용하여 방문한 노드 처리
def other_solution(n, costs):
    costs.sort(key=lambda x: x[2])
    node = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]

    while len(node) != n:
        for i in range(1, len(costs)):
            if costs[i][0] in node and costs[i][1] in node:
                continue
            if costs[i][0] in node or costs[i][1] in node:
                node.update([costs[i][0], costs[i][1]])
                answer += costs[i][2]
                break

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
print(other_solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
