# first and last position of an element in sorted array

from math import ceil

def firstoccurance(a,key):
    start=0
    end=len(a)-1

    while start<=end:
        mid=ceil((start+end)/2)
        if key==a[mid]:
            ans=mid
            end=mid-1
        elif key<a[mid]:  ##key is smaller than mid
            end=mid-1
        elif key>a[mid]: ## key is bigger than mid
            start=mid+1

    return ans

def lastoccurance(a,key):
    start=0
    end=len(a)-1

    while start<=end:
        mid=ceil((start+end)/2)
        if key==a[mid]:
            ans=mid
            start=mid+1
        elif key<a[mid]:
            end=mid-1
        elif key>a[mid]:
            start=mid+1

    return ans

a = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8,9]
key=4

print("first occurance of {}={}".format(key,firstoccurance(a,key)))
print("last occurance of {}={}".format(key,lastoccurance(a,key)))

number_of_occurance=(lastoccurance(a,key)-firstoccurance(a,key))+1
print("number of occurance of {}={}".format(key,number_of_occurance))


        



        