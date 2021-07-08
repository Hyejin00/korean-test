n = input()
num = ""
is_minus = False
ans = 0
for i in n:
  if is_minus:
    if i in '-+':
      ans -= int(num)
      num = ""
    else:
      num += i
  else:
    if i == '-':
      is_minus =True
      ans += int(num)
      num = ""
    elif i == '+':
      ans += int(num)
      num = ""
    else:
      num += i
if is_minus:
  ans -= int(num)
else:
  ans += int(num)
print(ans)