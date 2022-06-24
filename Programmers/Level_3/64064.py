from itertools import permutations


def chk(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    per = list(permutations(user_id, len(banned_id)))
    ban_set = []

    for users in per:
        if not chk(users, banned_id):
            continue
        else:
            users = set(users)

            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)


u0 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
u1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
u2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b0 = ["fr*d*", "abc1**"]
b1 = ["*rodo", "*rodo", "******"]
b2 = ["fr*d*", "*rodo", "******", "******"]
print(solution(u0, b0))
print(solution(u1, b1))
print(solution(u2, b2))
