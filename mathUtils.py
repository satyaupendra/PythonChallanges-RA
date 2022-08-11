def powerOfNumber (base, exponent):
    result = 1
    for exponent in range(exponent,0,-1):
        result = result * base
    return result
def factorialOfNumber(n):
    factorial=1
    if(n<0):
        return 0
    if (n==1 or n==0):
        return 1
    else:
        for i in range(1,n + 1):
            factorial = factorial*i
        return factorial

def sumOfNumbers(n):
    sum = 0 
    for i in range(1,n+1):
        sum = sum +i
    return sum

