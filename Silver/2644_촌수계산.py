import sys
sys.stdin = open('2644_촌수계산.txt')

def find_root(n, lst):

    if parent[n] == 0:
        return
    else:
        lst.append(parent[n])
        find_root(parent[n], lst)




n = int(input())                # 사람의 수

h1, h2 = map(int, input().split())   # 관계를 알고싶은 사람 두 명

m = int(input())                # 관계의 수

parent = [0] * (n + 1)
flag = False
res = 0
for _ in range(m):
    a, b = map(int, input().split())
    parent[b] = a

lst1 = []
lst2 = []
lst1.append(h1)
lst2.append(h2)
find_root(h1, lst1)
find_root(h2, lst2)

for i in range(len(lst1)):
    if flag == True:
        break
    else:
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                res = i + j
                flag = True
                break
else:
    if not res:
        res = -1
print(res)