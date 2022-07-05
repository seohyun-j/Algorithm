import sys

sys.setrecursionlimit(10 ** 6)


def preorder(arrY, arrX, pre):
    root = arrY[0]
    idx = arrX.index(root)
    left = []
    right = []

    for i in range(1, len(arrY)):
        if root[0] > arrY[i][0]:
            left.append(arrY[i])
        else:
            right.append(arrY[i])

    pre.append(root[2])

    if len(left) > 0:
        preorder(left, arrX[:idx], pre)

    if len(right) > 0:
        preorder(right, arrX[idx + 1:], pre)

    return


def postorder(arrY, arrX, post):
    root = arrY[0]
    idx = arrX.index(root)
    left = []
    right = []
    for i in range(1, len(arrY)):
        if root[0] > arrY[i][0]:
            left.append(arrY[i])
        else:
            right.append(arrY[i])

    if len(left) > 0:
        postorder(left, arrX[:idx], post)
    if len(right) > 0:
        postorder(right, arrX[idx + 1:], post)

    post.append(root[2])
    return


def solution(nodeinfo):
    pre = []
    post = []

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    arrY = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    arrX = sorted(nodeinfo)

    preorder(arrY, arrX, pre)
    postorder(arrY, arrX, post)

    return [pre, post]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
