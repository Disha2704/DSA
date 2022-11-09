
def peakElement(a,start,end):
    while start<=end:

        mid=((start+end)//2)
        if a[mid]>a[mid+1] and a[mid]>a[mid-1]:
            print("{} is peak".format(a[mid]))
            print("peak element is present at index {} ".format(mid))
            break
        elif a[mid]<a[mid-1]:
            end=mid-1
        elif a[mid]<a[mid+1]:
            start=mid+1

def minimumElement(a):
    min1=a[0]
    min2=a[-1]
    if min1<min2:
        min=min1
    else:
        min=min2

    print("minimum number in the array is {}".format(min))
            
            

a=[2,4,5,4,3]
start=0
end=len(a)-1
peakElement(a,start,end)
minimumElement(a)


    