p0 = ["119", "97674223", "1195524421"]
p1 = ["123", "456", "789"]
p2 = ["12", "123", "1235", "567", "88"]


def solution(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


print(solution(p0))
print(solution(p1))
print(solution(p2))
