n,m = map(int, input().split())

result = []
for i in range(n):
    v = list(map(int, input().split()))
    v.sort()
    result.append(v[0])

result.sort(reverse=True)
print(result[0])