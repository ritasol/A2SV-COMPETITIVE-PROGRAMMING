n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
if k == 0:
    if a[0] <= 1:
        print(-1)
    else:
        print(1)
else:
    cnt = 0
    num = a[k-1]
    for i in range(n):
        if a[i] > num:
            break
        cnt += 1
    if cnt == k:
        print(num)
    else:
        print(-1)
