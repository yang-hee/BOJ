import sys
sys.stdin = open('input.txt')

low = 0
high = 11
# lying = False

while True:
    a = int(input())
    if a == 0:
        break
    b = input()
    if b == 'too high':
        if high > a:
            high = a
    elif b == 'too low':
        if low < a:
            low = a
    else:
        ## 입력 값이 high나 low값을 벗어나거나 high와 low의 차이가 나지 않을때(high = 6이고 low = 5이면 사이에 정답값이 있을 수가 없다..!)
        if (a >= high or a <= low) or (high - low) <= 1:
            print('Stan is dishonest')
        else:
            print('Stan may be honest')
        ## 테스트케이스가 여러개 있는 경우를 위해 high와 low값 초기화
        high = 11
        low = 0




# low = 1
# high = 10
# a = False
#
# while True:
#     qus = int(input())
#     if qus == 0:
#         break
#     ans = input()
#     if ans == 'right on':
#         if not a:
#             if low < qus < high:
#                 print('Stan may be honest')
#             else:
#                 print('Stan is dishonest')
#         else:
#             print('Stan is dishonest')
#         a = False
#         low = 1
#         high = 10
#
#     elif ans == 'too high':
#         if qus >= high:
#             a = True
#         high = qus
#     elif ans == 'too low':
#         if qus <= low:
#             a = True
#         low = qus