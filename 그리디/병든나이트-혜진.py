n, m = map(int, input().split())

if n == 1:
  ans = 1
elif n == 2:
  ans = 4 if m >= 7 else (m+1)//2
elif n >= 3:
  if m >= 7:
    ans = m-2
  else:
    ans = m if m <= 4 else 4
print(ans)