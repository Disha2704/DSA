import array as arr

array=arr.array("i",[1,2,3,4,5,6,7])
key=9
def search(array):
    for i in range(len(array)):
        if array[i]==key:
            print("key is present at index {}".format(i))
        else:
            print("key not found")
            break

search(array)
