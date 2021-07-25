from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001

def bfs():
  queue = deque([(n,0)])
  while queue:
    val, cnt = queue.popleft()
    if val == k:
      return cnt
    if not visited[val]:
      visited[val] = True
      if val+1 <= 100000:
        queue.append((val + 1, cnt + 1))
      if val*2 <= 100000:
        queue.append((val * 2, cnt + 1))
      if val > 0:
        queue.append((val - 1, cnt + 1))
ans = 0 if n==k else bfs()
print(ans)