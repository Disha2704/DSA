# whether character  is numberlowe-case/upper-case

char=input("enter character")

if ord(char)>65 and ord(char)<90:
    print("{} is in upper case".format(char))

elif ord(char)>97 and ord(char)<122:
    print("{} is in lower case".format(char))

else:
    print("{} is a number or any other character".format(char))

