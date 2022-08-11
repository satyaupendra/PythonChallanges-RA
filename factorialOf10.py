from math import prod


n=10
product=1
for i in range(1,n+1):
    product = product * i
print("Factorial of {n} is {product}".format(n=n,product=product))