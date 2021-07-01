n, k = map(int, input().split())
ans = 0

while n >= k:
  ans += n % k
  n = n//k
  ans += 1

if n > 1:
  ans += n-1

print(ans)