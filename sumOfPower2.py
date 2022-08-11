from mathUtils import powerOfNumber
n=400
sum = 0
for i in range(1,n+1):
    temp = powerOfNumber(i,2)
    sum = sum + temp
    print("Sum of powers of first {n} numbers is {res}".format(n=i,res=sum))
print("Sum of Powers of 400 numbers is :",sum)
