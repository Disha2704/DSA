import array as arr


a=arr.array("i",[1,2,3,4,5])
# i=len(a)-1
# while i>=0:
#     print(a[i])
#     i=i-1

start=0
end=len(a)-1

while start<=end:
    a[start],a[end]=a[end],a[start]
    start=start+1
    end=end-1
    
print(a)