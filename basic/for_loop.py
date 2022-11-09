a=0
b=1
n=int(input("till how many number?"))
print(a,b,end=" ")
for i in range(n-2):
    sum=a+b
    print(sum,end=" ")
    a=b
    b=sum