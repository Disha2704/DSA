a=[2,2,2,1,1,1,0]
count=[]

count0=0
count1=0
count2=0

for i in a:
    if i==0:
        count0=count0+1
    elif i==1:
        count1=count1+1
    else:
        count2=count2+1
print(count0,count1,count2)