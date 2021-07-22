from collections import deque

n, m, v = map(int, input().split())
graph = [set() for _ in range(n+1)]

for _ in range(m):
  v1, v2 = map(int, input().split())
  graph[v1].add(v2)
  graph[v2].add(v1)
graph = list(map(list, graph))

for i in range(n+1):
  graph[i].sort()

def dfs(n, visited):
  visited.append(n)
  for v in graph[n]:
    if v not in visited:
      dfs(v,visited)
  return visited

def bfs(n):
  queue = deque()
  queue.append(n)
  visited = []
  visited.append(n)
  while queue:
    v = queue.popleft()
    for val in graph[v]:
      if val not in visited:
        queue.append(val)
        visited.append(val)
  return visited

dfs = dfs(v, [])
bfs = bfs(v)
for i in dfs:
  print(i, end= " ")
print()
for i in bfs:
  print(i, end=" ")