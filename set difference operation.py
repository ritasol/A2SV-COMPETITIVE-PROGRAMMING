E = int(input())
lst_E = list(input().split())
F = int(input())
lst_F = list(input().split())

cnt = 0
for i in lst_E:
    if i not in lst_F:
        cnt += 1
print(cnt)