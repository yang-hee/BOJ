#시험점수 등급판별
A = int(input())

if A >= 90:
    print('A')
elif A >= 80: # if문으로 90이상인 조건이 빠졌으므로 90 > A 안해줘도 됨!
    print('B')
elif A >= 70:
    print('C')
elif A >= 60:
    print('D')
else:
    print('F')