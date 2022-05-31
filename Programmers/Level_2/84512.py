words = ["AAAAE", "AAAE", "I", "EIO"]

from itertools import product
def solution(word):
    list1 = ['A', 'E', 'I', 'O', 'U']
    list2 = list(product(list1, repeat=2))
    list3 = list(product(list1, repeat=3))
    list4 = list(product(list1, repeat=4))
    list5 = list(product(list1, repeat=5))
    arr = list1 + list2 + list3 + list4 + list5
    arr = [''.join(i) for i in arr]
    arr.sort()
    return arr.index(word)+1

for i in words:
    print(solution(i))