# n=6
"""



"""


a=[1,1,2,3,4,5]
repeating_number=[]
for i in a:
    if i not in repeating_number:
        repeating_number.append(i)
    else:
        print(i)
        break

a=[1,2,3,4,5]

i=0
while i<len(a):
    if (i+1)<len(a):
        a[i],a[i+1]=a[i+1],a[i]
        
    i=i+2
print(a)