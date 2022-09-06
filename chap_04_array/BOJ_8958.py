import sys
sys.stdin=open('BOJ_8958.txt')
T = int(input())
for tc in range(T):
    lst = input()

    count = 0
    count_lst = []
    for i in lst:
        if i == 'O':
            count +=1
        elif i == 'X' and count != 0:
            count_lst.append(count)
            count = 0
        else:
            count = 0
    else:
        if count != 0:
            count_lst.append(count)
    result = 0
    for j in count_lst:
        for k in range(1, j + 1):
            result += k

    print(result)

    # ox = input()
    # result = 0
    # count = 0
    # for i in ox:
    #     if i == 'O':
    #         count += 1
    #         result += count
    #     else:
    #         count = 0
    # print(result)
