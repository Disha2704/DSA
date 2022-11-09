import array as arr
import numpy as np
a=arr.array("i",[1,2,3,4,5])

for i in range(0,len(a),2):
    if (i+1<len(a)):
        # a[i],a[i+1]=a[i+1],a[i]
        temp=a[i+1]
        a[i+1]=a[i]
        a[i]=temp

    
print(np.array(a))

