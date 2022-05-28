n0 = 3
n1 = 5
n2 = 2
word0 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
word1 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure",
         "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
word2 = ["hello", "one", "even", "never", "now", "world", "draw"]


def solution(n, words):
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in words[:i]:
            return [i % n + 1, i // n + 1]
    return [0, 0]


print(solution(n0, word0))
print(solution(n1, word1))
print(solution(n2, word2))
