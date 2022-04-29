import sys
input = sys.stdin.readline

n, q = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n**2)]
L = int(input())
