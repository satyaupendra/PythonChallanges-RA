n=300
sum = 0
for i in range(1,n+1):
	sum = sum + i
	if sum <= 40000:
		print("Sum of the first {i} terms is {sum}".format(i=i,sum=sum))
	else:
		print("Sum of the first {i} terms is over 40000".format(i=i))