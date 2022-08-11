n = 15
for i in range(n+1):
    factorial = 1
    if i < 0:
        print("n must be non negative number")
    elif i == 0:
        print("1")
    else:
        for j in range(1,i+1):
            factorial = factorial*j
        print("The value of {n} factorial is {factorial}".format(n=i,factorial=factorial))