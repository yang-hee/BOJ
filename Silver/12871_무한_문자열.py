import sys
sys.stdin = open('input.txt')


s = input()
t = input()
if s * len(t) == t * len(s):
    print(1)
else:
    print(0)

## abab / ababab 의 경우 같은 문자열을 만든다.. 고려 안한 코드
# if len(s) >= len(t):
#     if s == t * (len(s) // len(t)):
#         print(1)
#     else:
#         print(0)
# elif len(t) > len(s):
#     if t == s * (len(t) // len(s)):
#         print(1)
#     else:
#         print(0)

# res = -1
# length = 0
# if len(s) > len(t):
#     length = len(s)
# else:
#     length = len(t)
# print()
# for i in range(length):
#     if s[i] != t[i]:
#         res = 0
#         break
#