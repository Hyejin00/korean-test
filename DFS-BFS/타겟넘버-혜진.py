def solution(numbers, target):
  answer = 0
  def dfs (sum, idx):
    nonlocal answer
    if idx >= len(numbers):
      if sum == target:
        answer += 1
      return
    dfs(sum + numbers[idx], idx + 1)
    dfs(sum - numbers[idx], idx + 1)
  dfs(0, 0)
  return answer