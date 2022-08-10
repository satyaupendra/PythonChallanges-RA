def powerOfNumber (base, exponent):
    result = 1
    for exponent in range(exponent,0,-1):
        result = result * base
    return result
def factorialOfNumber(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * factorialOfNumber(n - 1)