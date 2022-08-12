sum = 0
i=0
while (sum < 15):
    i=i+1
    sum = sum + (1/i)
print("Last value added to sum :", 1/(i-1))
print("Number of terms to make sum greater than 15", i-1)
print("Value of Sum : %0.30f "%(sum))
