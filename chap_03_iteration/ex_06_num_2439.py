# N = int(input())
# star = '*'
# while len(star) <= N:
#     print(f"{(' '*N-len(star))}{star}")
#     star += '*'

N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)
