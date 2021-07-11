def solution(brown, yellow):
  answer = []
  end = int(brown/2)+2
  for i in range(3, end):
    if (i-2)*(end-i-2) == yellow:
      answer.append(i)
      answer.append(end-i)
      break
  answer.sort(reverse=True)
  return answer