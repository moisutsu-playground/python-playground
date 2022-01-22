n = int(input())

total = 0

for i in range(1, n + 1):
    total += i
    if total >= n:
        print(i)
        break
