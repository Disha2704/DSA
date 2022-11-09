a=[5 ,1 ,2 ,3 ,4 ,2  ]
b=[8, 7, 2 ,5, 4, 7, 1 ,3, 6]

intersection_list=[]
for i in a:
    if i in b:
        intersection_list.append(i)
final_list=[]
for i in intersection_list:
    if i not in final_list:
        final_list.append(i)
print(final_list)