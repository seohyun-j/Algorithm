from collections import Counter

cnt = Counter(input())
if sum(c % 2 for c in cnt.values()) > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''

    for val, idx in sorted(cnt.items()):
        half += val * (idx // 2)

    answer = half

    for val, idx in cnt.items():
        if idx % 2:
            answer += val
            break

    answer += ''.join(reversed(half))
    print(answer)
