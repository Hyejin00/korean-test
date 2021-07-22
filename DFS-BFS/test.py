a = 1
def abc():
  global a
  if a == 1:
    a = a+1
    print("TRUE")
abc()
print(a)