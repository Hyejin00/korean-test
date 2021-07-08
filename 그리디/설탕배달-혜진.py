n = int(input())
ans = -1
for i in range(0, (n//3)+1):
    for j in range(n//5, -1,-1):
        if 3*i + 5*j == n:
            ans = i+j
            break
    if ans != -1:
        break
print(ans)