# MAX VALUE IN ARRAY
import array as arr
a=arr.array("i",[8,7,6,5,1,2,3])

max=a[0]
min=a[0]

for i in range(1,len(a)):
    if a[i]>max:
        max=a[i]
for i in range(1,len(a)):
    if a[i]<min:
        min=a[i]
        
print(max)
print(min)