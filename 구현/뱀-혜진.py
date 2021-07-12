from collections import deque

n = int(input())
k = int(input())

graph = [[0]*n for _ in range(n)]

for _ in range(k):
  r, c = map(int, input().split())
  graph[r-1][c-1] = 'A'

L = int(input())
turn = {}
for _ in range(L):
  t, rl = input().split()
  turn[int(t)] = rl

head = [0,0]
tail = [0,0]
graph[0][0] = '-'
# 오른쪽, 밑, 왼쪽, 위
directions = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0
sec = 0
queue = deque()

def turn_lr(direction):
  global d
  if direction == 'L':
    d -= 1
    if d <= -1:
      d = 3
  if direction == 'D':
    d += 1
    if d >= 4:
      d = 0
while True:
  sec += 1
  dx, dy = head[0] + directions[d][0], head[1] + directions[d][1]
  queue.append((directions[d][0],directions[d][1]))
  if not (-1 < dx < n) or not (-1 < dy < n) or graph[dx][dy] == '-':
    break
  if graph[dx][dy] != 'A':
    graph[tail[0]][tail[1]] = 0
    dt = queue.popleft()
    tail[0] += dt[0]
    tail[1] += dt[1]
  graph[dx][dy] = '-'
  head[0], head[1] = dx, dy
  if sec in turn:
    turn_lr(turn[sec])
print(sec)