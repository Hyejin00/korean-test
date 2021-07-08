def solution(n, lost, reserve):
  temp = set(lost) & set(reserve)
  lost = list(set(lost) - temp)
  reserve = list(set(reserve) - temp)
  for i in lost[:]:
      if i-1 in reserve:
          lost.remove(i)
          reserve.remove(i-1)
          continue
      if i+1 in reserve:
          lost.remove(i)
          reserve.remove(i+1)
      print(lost,)
  return n - len(lost)