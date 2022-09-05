#합 출력 while문 이용
T = int(input()) # Testcase
test_case = 1

while test_case <= T :
    A, B = map(int, input().split())
    print(A + B)
    test_case += 1


'''합 출력 for문 이용   
T = int(input())

for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(A + B)
'''