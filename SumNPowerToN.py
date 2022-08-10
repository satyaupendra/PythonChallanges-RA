from mathUtils import powerOfNumber

n = int(input("Enter the value of n : "))
sum = 0
for i in range(1,n+1):
    temp = powerOfNumber(i,i)
    print("{n} power {n} is {temp}".format(n=i,temp=temp))
    sum = sum +temp
    print("Sum of Nth powers of first {e} numbers is : {sum}".format(e=i,sum=sum))
print("Sum of Series N to Power N: ",sum)
    