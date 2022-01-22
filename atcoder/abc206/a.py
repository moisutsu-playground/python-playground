import math

n = int(input())

price = math.floor(n * 1.08)

if price < 206:
    print("Yay!")
elif price == 206:
    print("so-so")
else:
    print(":(")
