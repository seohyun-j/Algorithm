arr = [1, 5, 2, 6, 3, 7, 4]
com = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


# reply = sorted(array[i[0]-1:i[1]]) 보다 reply 선언 후 sort() 이용하는 것이 더 빠르다.
def solution(array, commands):
    answer = []
    for i in commands:
        reply = array[i[0] - 1:i[1]]
        reply.sort()
        answer.append(reply[i[2] - 1])
    return answer


print(solution(arr, com))
