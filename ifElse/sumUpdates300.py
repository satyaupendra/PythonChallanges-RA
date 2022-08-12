sum = 0
n= 300
for i in range(1,n+1):
    sum = sum + i
    if i/20 == int(i/20.0):
        print("Sum of the first {i} terms is {sum}".format(i=i,sum=sum))
