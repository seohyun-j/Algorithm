t = 0
while True:
    L, P, V = map(int, input().split())
    if [L, P, V] == [0, 0, 0]:
        break

    t += 1
    day = V // P * L + min(V % P, L)

    print(f'Case {t}: {day}')