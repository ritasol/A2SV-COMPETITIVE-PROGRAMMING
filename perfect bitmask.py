t = int(input())
for _ in range(t):
	a=int(input())
	neg = -a
	b=a&neg
	while (a==b or (a&b)==0):
		b+=1
	print(b)
