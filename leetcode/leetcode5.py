# import array as arr

# a=arr.array("i",[1,2,2,3,3,4,5])

a=[1,2]
unique_elements=[]
for i in a:
    if i not in unique_elements:
        unique_elements.append(i)
print(unique_elements)

count_list=[]
for i in unique_elements:
    count=0
    for j in range(len(a)):
        if i==a[j]:
            count=count+1
    count_list.append(count)
print(count_list)

final_list=[]
flag=True
for i in count_list:
    if i not in final_list:
        final_list.append(i)
        # print("true")    
    else:
        flag=False
        break
if flag==False:
    print("false")
else:
    print("true")