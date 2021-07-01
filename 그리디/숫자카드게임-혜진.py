n, m = map(int, input().split())
t = []
for _ in range(n):
  t.append(list(map(int, input().split())))

max_n = 1
for i in t:
  min_n = min(i)
  if min_n> max_n:
    max_n = min_n

print(max_n)