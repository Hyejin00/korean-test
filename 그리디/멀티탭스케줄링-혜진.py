n, k = map(int, input().split())
a = list(map(int, input().split()))
plug = []
ans = 0
for i in range(len(a)):
  if a[i] in plug:
    continue
  elif len(plug) < n:
    plug.append(a[i])
  else:
    rank = [101] * len(plug)
    for j in range(n):
      if plug[j] in a[i:]:
        rank[j] = a[i:].index(plug[j])
    plug[rank.index(max(rank))] = a[i]
    ans += 1
print(ans)