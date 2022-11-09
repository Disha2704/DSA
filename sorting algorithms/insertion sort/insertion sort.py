
def InsertionSort(a):
    for i in range(1,len(a)):
        temp=a[i]
        j = i-1
        while j >= 0 and temp < a[j] :
            a[j + 1] = a[j]
            j =j-1
            a[j + 1] = temp

    print(a)

a=[5,3,4,1,2]
InsertionSort(a)
  





























