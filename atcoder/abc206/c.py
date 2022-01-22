n = int(input())
a_s = [int(a) for a in input().split()]

map = dict()

for a in a_s:
    map[a] = map[a] + 1 if a in map else 1

ans = 0

for value in map.values():
    ans += (n - value) * value

print(ans // 2)
