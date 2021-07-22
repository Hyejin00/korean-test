def solution(tickets):
  ticks = {}
  for t1, t2 in tickets:
      ticks[t1] = ticks.get(t1,[]) + [t2]
  for tick in ticks:
      ticks[tick].sort(reverse=True)

  stack = ["ICN"]
  answer = []
  while stack:
      v = stack[-1]
      if v in ticks and len(ticks[v]) > 0:
          stack.append(ticks[v].pop())
      else:
          answer.append(stack.pop())
  answer.reverse()
  return answer

solution([["ICN", "AOO"], ["ICN", "AOO"], ["AOO", "ICN"], ["AOO", "COO"]])