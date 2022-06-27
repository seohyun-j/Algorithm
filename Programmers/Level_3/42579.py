def solution(genres, plays):
    answer = []
    dic = {i: 0 for i in set(genres)}
    playlist = {i: [] for i in set(genres)}

    for i, (g, p) in enumerate(zip(genres, plays)):
        dic[g] += p
        playlist[g].append((i, p))

    for (k, v) in sorted(dic.items(), key=lambda x: (-x[1])):
        for (i, p) in sorted(playlist[k], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(i)

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
