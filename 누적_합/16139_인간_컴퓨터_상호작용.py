import sys
sys.stdin=open('16139_인간_컴퓨터_상호작용.txt')

S = sys.stdin.readline().rstrip()           # 문자열, 소문자로만 구성됨
q = int(sys.stdin.readline())
res = []
string = ''
for i in S:
    string += i
    res.append(string)

for i in range(q):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    if l == 0:
        ss = res[r]
    else:
        ss = res[r].lstrip(res[l - 1])
    print(ss.count(a))
