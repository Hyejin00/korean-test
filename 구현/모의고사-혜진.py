def solution(answers):
  p = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
  cnts = [0,0,0]
  for idx, answer in enumerate(answers):
    for i in range(3):
      if p[i][idx % len(p[i]) if idx > 0 else idx] == answer:
        cnts[i] += 1
  answer = []
  max_num = max(cnts)
  for idx, cnt in enumerate(cnts):
    if cnt == max_num:
        answer.append(idx+1)
  answer.sort()
  return answer