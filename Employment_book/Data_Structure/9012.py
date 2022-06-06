for i in range(int(input())):
    arr = []
    answer = 'YES'
    for j in input():
        if j == '(':
            arr.append(j)
        else:
            if len(arr) > 0:
                arr.pop()
            else:
                answer = 'NO'

    if len(arr) > 0:
        answer = 'NO'
    print(answer)