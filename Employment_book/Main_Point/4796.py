t = 0
while True:
    L, P, V = map(int, input().split())
    if [L, P, V] == [0, 0, 0]:
        break

    t += 1
    day = L * V // P + min(V % P, L)

    print("Case " + str(t) + ': ' + str(day))