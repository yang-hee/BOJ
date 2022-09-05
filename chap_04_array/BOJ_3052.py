import sys
sys.stdin = open('BOJ_3052.txt')

lst = []
for _ in range(10):
    lst.append(int(input()))

lst2 = []
for i in lst:
    lst2.append(i % 42)

print(len(set(lst2)))

