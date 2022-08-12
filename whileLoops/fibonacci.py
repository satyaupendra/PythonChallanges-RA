previous = 1
current = 1
sum =0
counter  = 3
print("Position {pos} in the Fibonacci sequence is {val}".format(pos=1, val=previous))
print("Position {pos} in the Fibonacci sequence is {val}".format(pos=2, val=counter))
while sum < 10000:
    sum = previous+current
    print("Position {pos} in the Fibonacci sequence is {val}".format(pos=counter, val=sum))
    previous=current
    current=sum
    counter = counter +1