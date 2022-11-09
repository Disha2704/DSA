a=[6,2,8,4,4,10]

for i in range(len(a)):
    minIndex=i
    for j in range(i+1,len(a)):
        if (a[j]<a[minIndex]):
            minIndex=j
        
    a[i],a[minIndex]=a[minIndex],a[i]

print(a)

