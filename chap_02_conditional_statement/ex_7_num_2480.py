#주사위 상금
a, b, c = map(int, input().split())

price = 0

if a == b == c:
    price = 10000 + (a * 1000)

elif a == b:
    price = 1000 + (a * 100)

elif a == c:
    price = 1000 + (a * 100)

elif b == c:
    price = 1000 + (c * 100)

else:
    price = max(a, b, c) * 100

print(price)