import sys
sys.stdin = open('input.txt')

X, Y, W, S = map(int, input().split())
res = 0

# 대각선 이동보다 X, Y 한 블록씩 가는게 효율적인 경우
if (W * 2) < S:
    res = (X + Y) * W
else:
    if X > Y:
        if W > S:
            if (X - Y) % 2:
                res = (Y * S) + ((X - Y - 1) * S) + W
            else:
                res = (Y * S) + ((X - Y) * S)
        else:
            res = (Y * S) + (X - Y) * W
    else:
        if W > S:
            if (Y - X) % 2:
                res = (X * S) + ((Y - X - 1) * S) + W
            else:
                res = (X * S) + ((Y - X) * S)
        else:
            res = (X * S) + (Y - X) * W
print(res)