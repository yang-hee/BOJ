import sys
sys.stdin=open('13305_주유소.txt')

N = int(input())                            # 도시의 개수
road = list(map(int, input().split()))      # 도로의 길이
price = list(map(int, input().split()))     # 마을 주유소 가격

res = 0
low_price = price[0]
for i in range(N-1):
    if low_price > price[i+1]:
        res += road[i] * low_price
        low_price = price[i+1]
    else:
        res += road[i] * low_price
print(res)

