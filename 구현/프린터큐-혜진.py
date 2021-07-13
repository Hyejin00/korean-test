from collections import deque
c = int(input())
ans = []
for _ in range(c):
  n, m = map(int, input().split())
  orders = deque(list(map(int, input().split())))
  cnt = 0
  while True:
    if orders[0] == max(orders):
      orders.popleft()
      cnt += 1
      if m == 0:
        ans.append(cnt)
        break
      m -= 1
    else:
      orders.append(orders.popleft())
      if m == 0:
        m = len(orders)
      m -= 1

for a in ans:
  print(a)