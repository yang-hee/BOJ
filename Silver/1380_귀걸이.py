import sys
sys.stdin = open('1380_귀걸이.txt')

test_num = 1
while True:
    cnt_std = int(input())

    if cnt_std == 0:
        break

    else:

        lst_std = list(input() for _ in range(cnt_std))
        dic_std = {}
        for i in range(2 * cnt_std - 1):
            a, b = input().split()
            if a in dic_std:
                del(dic_std[a])
            else:
                dic_std[a] = b
        idx = list(dic_std.keys())
        idx = int(idx[-1])

        print(test_num, lst_std[idx - 1])
        test_num += 1
            # else:
            #




