import sys
sys.stdin = open('input.txt')
import math

a, b = map(int, input().split())
print(a * b // math.gcd(a, b))