n = int(input())

time_table = []
for _ in range(n):
  time_table.append(tuple(map(int, input().split())))
time_table.sort(key=lambda x:(x[1],x[0]))
print(time_table)

ans = 1

end = time_table[0][1]

for i in time_table[1:]:
  if i[0] >= end:
    end = i[1]
    print(end)
    ans += 1

print(ans)