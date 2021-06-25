n, m, k = list(map(int, input().split()))
num = list(map(int, input().split()))

num.sort(reverse=True)

ans = num[0]
m -= 1
cnt = 1
while m > 0:
  if cnt % k == 0:
    ans += num[1]
  else:
    ans += num[0]
  cnt += 1
  m -= 1

print(ans)