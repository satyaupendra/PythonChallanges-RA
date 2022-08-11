sum = 0
n = int(input("Enter the value of n : "))
for i in range(n+1):
  temp = 1
  for j in range(1,i+1,1):
    temp = temp * j
  sum = sum + 1.0/temp
  print("Sum of after first {i} terms is {sum}".format(i=i+1, sum=format(sum,".6f")))
  print("Latest term is {temp}".format(temp=format(1/temp, ".5f")))

  # I have obsereved that after the sum of first 10 numbers the approximate value of taylor series is 2.71828,
  #  for larger values of n (n> 18) it becomes constant value which is 2.7182818284590455...