#틀림
n, k = map(int, input().split())
a = list(map(int, input().split()))
plug = [a[i] for i in range(n)]
ans = 0
for i in range(n, len(a)):
  if a[i] in plug:
    continue
  else:
    rank = [101]*n
    for j in range(n):
      if plug[j] in a[i:]:
        rank[j] = a[i:].index(plug[j])
    plug[rank.index(max(rank))] = a[i]
    ans += 1
print(ans)