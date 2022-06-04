a01 = [[1, 4], [3, 2], [4, 1]]
a02 = [[3, 3], [3, 3]]
a11 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
a12 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]


def solution(arr1, arr2):
    answer = [len(arr2[0]) * [0] for i in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            for k in range(len(arr1[i])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


import numpy as np


def np_solution(arr1, arr2):
    return np.dot(arr1, arr2).tolist()


print(solution(a01, a02))
print(solution(a11, a12))
