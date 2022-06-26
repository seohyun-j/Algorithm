from collections import deque


def solution(begin, target, words):
    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))

    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            tmp_cnt = 0
            if not visited[i]:
                for p1, p2 in zip(word, words[i]):
                    if p1 != p2:
                        tmp_cnt += 1
                if tmp_cnt == 1:
                    visited[i] = True
                    queue.append((words[i], cnt + 1))

    return 0


w0 = ["hot", "dot", "dog", "lot", "log", "cog"]
w1 = ["hot", "dot", "dog", "lot", "log"]
print(solution("hit", "cog", w0))
print(solution("hit", "cog", w1))
