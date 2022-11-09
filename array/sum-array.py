# SUM OF ELEMENTS IN ARRAY

import array as arr
import numpy as np
size=int(input("how many elements in your array??"))
array=[] #list named as array
print("enter elements of array:-\n")
for i in range(size):
    element=int(input())
    array.append(element)
array=np.array(array) # converting list into array and store it in variable named as "arrays"
sum=0
for i in range(len(array)):
    sum=sum+array[i]

print("sum of elements of array is {}".format(sum))
