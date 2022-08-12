a=12
b=7
c=9
print("a={a}, b={b}, c={c}".format(a=a,b=b,c=c))

if a>b and a>c:
    if b>c:
        a1,b1,c1=a,b,c
    else:
        a1,b1,c1=a,c,b
elif b>a and b>c:
    if a>c:
        a1,b1,c1=b,a,c
    else:
        a1,b1,c1=b,c,a
else:
    if a>b:
        a1,b1,c1=c,a,b
    else:
        a1,b1,c1=c,b,a
print("Descending orde : ",a1,b1,c1)
