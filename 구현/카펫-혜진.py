def solution(brown, yellow):
  answer = []
  end = int(brown/2)+2
  for i in range(3, end):
    if (i-2)*(end-i-2) == yellow:
      if i > end-i:
        answer.append(i)
        answer.append(end-i)
      else:
        answer.append(end-i)
        answer.append(i)
      break
  return answer