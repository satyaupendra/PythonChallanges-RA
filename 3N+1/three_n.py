n = int(input("Enter Value of n:"))
counter  =0
maximum = n
while n > 1:
  if n % 2 == 0:
    n = n // 2
  else:
    n = 3 * n + 1
  maximum = max(n,maximum)
  print("Current value of n :",n)
  counter = counter+1
print("Count for n value to reach 1 is :",counter)
print("Maximum value of N before the program reaches N=1 is:",maximum)