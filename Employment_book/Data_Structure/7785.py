import sys

input = sys.stdin.readline

enter = set()

for i in range(int(input())):
    name, state = input().split()
    if state == 'enter':
        enter.add(name)
    else:
        if name in enter:
            enter.remove(name)

for i in sorted(enter, reverse=True):
    print(i)