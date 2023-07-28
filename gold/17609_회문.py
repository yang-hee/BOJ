import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    s = input()
    start = 0
    end = len(s) - 1
    cnt = 0
    res = 0
    while start < end:
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            cnt += 1

            start2 = start + 1
            end2 = end
            res2 = 3
            if s[start2] == s[end2]:
                while start2 < end2:
                    start2 += 1
                    end2 -= 1
                    if s[start2] != s[end2]:
                        res2 = 2
                        break
                else:
                    res2 = 1

            start3 = start
            end3 = end - 1
            res3 = 3
            if s[start3] == s[end3]:
                while start3 < end3:
                    start3 += 1
                    end3 -= 1
                    if s[start3] != s[end3]:
                        res3 = 2
                        break
                else:
                    res3 = 1

            if min(res2, res3) == 1:
                res = 1
                break
            else:
                res = 2
                break

    print(res)