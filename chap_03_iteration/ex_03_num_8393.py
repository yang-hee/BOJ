#1부터 n까지의 합 while문 이용
n = int(input())
n_sum = 0
n_first = 1
while n_first <= n:
    n_sum += n_first
    n_first += 1
print(n_sum)


'''1부터 n까지의 합 for문 이용
n = int(input())
n_sum = 0
for i in range(1, n + 1):
    n_sum += i

print(n_sum)
'''
