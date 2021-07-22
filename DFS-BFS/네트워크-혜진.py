from collections import deque
def solution(n, computers):
  answer = 0
  for i in range(n):
    queue = deque([i])
    change = False
    while queue:
      v = queue.popleft()
      for j in range(n):
        if computers[v][j] == 1:
          change = True
          queue.append(j)
          computers[v][j] = 0
    if change:
      answer += 1
  return answer