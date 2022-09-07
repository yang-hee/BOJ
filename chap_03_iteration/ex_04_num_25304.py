# X 총 금액, N 구매한 물건의 개수
X = int(input())
N = int(input())
result = 0
for i in range(N):
    buy = list(map(int, input().split()))
    result += buy[0] * buy[1]

if result == X:
    print('Yes')
else:
    print('No')
