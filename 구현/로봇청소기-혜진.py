n, m = map(int, input().split())
x, y, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

move = [(-1,0),(0,1),(1,0),(0,-1)]
ans = 1
maps[x][y] = 2

while True:
  for _ in range(4):
    d = 3 if d-1 < 0 else d-1 
    dx = x + move[d][0]
    dy = y + move[d][1]
    if maps[dx][dy] == 0:
      x = dx
      y = dy
      maps[x][y] = 2
      ans += 1
      break
  else:
    x = x - move[d][0]
    y = y - move[d][1]
    if maps[x][y] == 1:
      break

print(ans)