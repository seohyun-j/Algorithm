def solution(tickets):
    answer = []
    stk = ["ICN"]
    dic = {}
    for s, e in tickets:
        if s in dic:
            dic[s].append(e)
        else:
            dic[s] = [e]

    for i in dic.keys():
        dic[i].sort(reverse=True)

    while stk:
        st = stk[-1]
        if st not in dic or len(dic[st]) == 0:
            answer.append(stk.pop())
        else:
            stk.append(dic[st].pop())
    return answer[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
