import sys
sys.stdin = open('BOJ_2562.txt')
lst = []
for i in range(9):
    lst.append(int(input()))

print(max(lst))
for j in range(len(lst)):
    if lst[j] == max(lst):
        print(j + 1)