n,m = map(int, input().split())

result = []
for i in range(n):
    value = list(map(int, input().split()))
    value.sort()
    result.append(value[0])

result.sort(reverse=True)
print(result[0])