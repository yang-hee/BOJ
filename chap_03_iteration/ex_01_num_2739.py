#구구단 while문 이용
N = int(input())
N_num = 1
while N_num < 10:
    print(f'{N} * {N_num} = {N * N_num}')
    N_num += 1

'''구구단 for문 이용
N = int(input())
for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')
'''