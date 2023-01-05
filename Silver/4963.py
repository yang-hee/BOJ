import sys
sys.setrecursionlimit(10**6)
sys.stdin=open('4963_섬의_개수.txt')

def find1(a, b):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]

    lst[a][b] = 3
    for i in range(8):
        nx = b + dx[i]
        ny = a + dy[i]
        if 0 <= ny <= h - 1 and 0 <= nx <= w - 1 and lst[ny][nx] == 1:
            find1(ny, nx)
    return

while True:
    w, h = map(int, input().split())
    cnt = 0


    if w == h == 0:
        break
    else:
        lst = [list(map(int, input().split())) for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if lst[i][j] == 1:
                    find1(i, j)
                    cnt += 1

        print(cnt)


