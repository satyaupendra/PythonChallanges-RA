n = int(input("Enter n value :"))
factorial = 1
if n < 0:
    print("n must be non negative number")
elif n == 0:
    print("1")
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print("The factorial of {n} is {factorial}".format(n=n,factorial=factorial))