

def pivotElement(a):
    start=0
    end=len(a)-1
    mid=((start+end)//2)
    while start<=end:
        if a[mid]>a[mid+1]:
            print("pivot element is {}".format(a[mid+1]))
            break
        else:
            mid=mid+1
a=[4,8,10,17,19,1,3]
pivotElement(a)
    
    
