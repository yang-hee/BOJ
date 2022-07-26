#사분면 판별 (x, y) 
# 제1사분면 : (+, +) / 제2사분면 : (-, +) / 제3사분면 : (-, -) / 제4사분면 : (+, -) 

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')