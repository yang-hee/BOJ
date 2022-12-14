import sys
sys.stdin=open('16139_인간_컴퓨터_상호작용.txt')

S = sys.stdin.readline().rstrip()           # 문자열, 소문자로만 구성됨
q = int(sys.stdin.readline())

print(chr(97))
for i in range(q):
    # alphabet 별로 구간합.. 구해놓고.. 출력할 때 한번에 되도록 해야지!
    a, l, r = sys.stdin.readline().split()

    print(a, l, r)


print(S, q)