import sys
sys.stdin = open('BOJ_4344.txt')

C = int(input())
for tc in range(C):
    lst = list(map(int, input().split()))

    # score(점수)랑 number(학생수)로 lst 인풋받은거 나눠줌
    score = []
    for i in range(len(lst)):
        if i == 0:
            number = lst[i]
        else:
            score.append(lst[i])

    # member는 평균넘는 학생 수!
    member = 0
    avg_score = sum(score) / number
    for j in score:
        if j > avg_score:
            member += 1
    result = member / number * 100
    print(f'{result:.3f}%')

