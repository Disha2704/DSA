a=[0,1,0,0,1,0,1,0]

i=0
j=len(a)-1

while i<j:
    if (a[i]==0):
        i=i+1
    elif (a[j]==1):
        j=j-1
    elif (a[i]==1 and a[j]==0):
        a[i],a[j]=a[j],a[i]
        i=i+1
        j=j-1
print(a)
    