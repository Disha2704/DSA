from math import ceil
a=[1,2,3,4,9,17,23,24]

key=9
start=0
end=len(a)-1

while start<=end:
    mid=ceil((start+end)/2)
    if key==a[mid]:
        print("key is present at {} index".format(mid))
        break
    elif key<a[mid]:
        end=mid-1
    elif key>a[mid]:
        start=mid+1
    


    