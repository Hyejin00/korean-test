n, m, k = map(int, input().split())
print(n, m, k)
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

r = 0
s = 0
for i in range(0, m):
    if s != k:
        s += 1
        r += data[0]
    else:
        s = 0
        r += data[1]

print(r)