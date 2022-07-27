def solution(s):
    def extract(word):
        cnt, stack = 0, []
        for i in word:
            if i == '0' and stack[-2:] == ['1', '1']:
                stack.pop()
                stack.pop()
                cnt += 1
            else:
                stack.append(i)
        return ''.join(stack), cnt

    def rearrange(word):
        for i in range(-1, -len(word) - 1, -1):
            pointer = len(word) + (i + 1)
            if word[i] == '0':
                return word[:pointer] + '110' + word[pointer:]
        return '110' + word

    answer = []
    for val in s:
        # 110 제거 하기
        val, count = extract(val)

        # 110 정렬하여 넣기
        for _ in range(count):
            val = rearrange(val)

        answer.append(val)
    return answer


print(solution(["1110", "100111100", "0111111010"]))
