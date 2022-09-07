import sys
sys.stdin=open('1271.txt')
A, B = map(int, input().split())
print(A // B)
print(A % B)