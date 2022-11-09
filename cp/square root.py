#4=2^2
#25=5^2

square=9
start=0
end=square//2
while start<=end:
    mid=((start+end)//2)
    if mid*mid==square:
        print("square root of {} is {}".format(square,ans))

        break
    elif mid*mid>square:
        end=mid-1
    elif mid*mid<square:
        start=mid+1
        ans=mid
    

    