N, X = map(int, input().split())

lst = list(map(int, input().split()))

result = []
for i in lst:
    if i < X:
        result.append(i)
print(*result)