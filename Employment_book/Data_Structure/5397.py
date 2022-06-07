for _ in range(int(input())):
    str = input()
    left = []
    right = []
    for i in str:
        if i == '-':
            if left:
                left.pop()
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(i)

    print(''.join(left) + ''.join(reversed(right)))
