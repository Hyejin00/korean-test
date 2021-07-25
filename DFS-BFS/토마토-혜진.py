from collections import deque

m, n, h = map(int, input().split())
tomato = []
for _ in range(h):
  arr2 = []
  for _ in range(n):
    arr2.append(list(map(int, input().split())))
  tomato.append(arr2)
#tomato[h][n][m]

steps = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]
def bfs(queue):
  while queue:
    qh, qn, qm = queue.popleft()
    for step in steps:
      vh = qh + step[0]
      vn = qn + step[1]
      vm = qm + step[2]
      if (-1 < vh < h) and (-1 < vn < n) and (-1 < vm < m):
        if tomato[vh][vn][vm] == 0:
          queue.append((vh, vn, vm))
          tomato[vh][vn][vm] = tomato[qh][qn][qm] + 1

queue = deque([])
for i in range(h):
  for j in range(n):
    for k in range(m):
      if tomato[i][j][k] == 1:
        queue.append((i, j, k))

bfs(queue)

max_num = -1
is_unriped = False
for arr2 in tomato:
  for arr in arr2:
    for a in arr:
      if a == 0:
        is_unriped = True
      else:
        max_num = max(max_num, a)

if is_unriped:
  print(-1)
elif max_num == 2:
  print(0)
else:
  print(max_num - 1)