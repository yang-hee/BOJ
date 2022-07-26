#오븐 요리종료 시간 알림
A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
    A += (B + C) // 60
    B = (B + C) % 60
    if A >= 24:
        A %= 24 

else:
    B = B + C

print(A, B)
