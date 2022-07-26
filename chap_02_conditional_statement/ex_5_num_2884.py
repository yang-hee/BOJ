#알람 45분 일찍 설정하기
H, M = map(int, input().split())

if H == 0 and M < 45:
    H = 23
    M += 15

elif M < 45:
    H -= 1
    M += 15

else:
    M -= 45

print(H, M)
