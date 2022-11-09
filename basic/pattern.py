"""
1.

$$$$
$$$$
$$$$
$$$$
n=int(input("box of ?"))
i=1
while i<=n:
    j=1
    while j<=n:
        print("* ",end=" ")
        j=j+1

    print("\n")
    i=i+1
"""

"""
2.

1 2 3 4
1 2 3 4
1 2 3 4

rows=int(input("how many rows u want?"))
columns=int(input("how many columns u want?"))
i=1
while i<=rows:
    j=1

    while j<=columns:
        print(j,end=" ")
        j=j+1

    print("\n")

    i=i+1

"""


"""
3.

123
456
789
rows=int(input("how many rows u want?"))
columns=int(input("how many columns u want?"))
i=1
n=1
while i<=rows:
    j=1
    while j<=columns:
        print(n,end=" ")
        n=n+1
        j=j+1
    print("\n")
    i=i+1

"""

"""
4.
*
**
***
****

rows=int(input("how many rows u want?"))
i=1
while i<=rows:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1

    print("\n")
    i=i+1
            
"""

"""
5.
1
22
333
4444
55555

rows=int(input("how many rows u want?"))
i=1
while i<=rows:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1

    print("\n")
    i=i+1

"""
"""
6.
1
2 3
4 5 6
7 8 9 10
rows=int(input("how many rows u want?"))
i=1
n=1
while i<=rows:
    j=1
    while j<=i:
        print(n,end=" ")
        n=n+1
        j=j+1
    print("\n")
    i=i+1
"""
"""
7.
1
2 3
3 4 5
4 5 6 7
rows=int(input("how many rows u want?"))
i=1
while i<=rows:
    j=1
    n=i
    while j<=i:
        print(n,end=" ")
        n=n+1
        j=j+1

    print("\n")
    i=i+1
"""
"""
8.
1        
2 1       
3 2 1     
4 3 2 1   
5 4 3 2 1

rows=int(input("how many rows u want?"))
i=1
while i<=rows:
    j=1
    n=i
    while j<=i:
        print(n,end=" ")
        n=n-1
        j=j+1

    print("\n")
    i=i+1       
"""
"""
9.
A B C D E 
A B C D E 
A B C D E 
A B C D E 
rows=int(input("how many rows u want?"))
columns=int(input("how many columns u want?"))
i=1
while i<=rows:
    c=65
    j=1
    while j<=columns:
        print(chr(c),end=" ")
        c=c+1
        j=j+1
    print("\n")
    i=i+1
"""
"""
A        
B C       
D E F     
G H I J   
K L M N O 
P Q R S T U
rows=int(input("how many rows u want?"))
i=1
c=65
while i<=rows:
    j=1
    while j<=i:
        print(chr(c),end=" ")
        c=c+1
        j=j+1
    print("\n")
    i=i+1
"""

"""
A B C
B C D
C D F
"""
"""
d
di
dis
dish
disha

str="disha"

j=1
while j<=len(str):
    k=0
    while k<j:
        print(str[k],end=" ")
        k=k+1
        
    print("\n")
    
    j=j+1

"""

"""
D
C D
B C D
A B C D
i=1
c=68
while i<=4:
    j=1
    while j<=i:
        print(chr(c),end=" ")
        c=c-1
        j=j+1

    print("\n")
    i=i+1
"""

"""
    *
   **
  ***   
 ****    
*****     

i=1
while i<=5:
    j=1
    while j<=(5-i):
        print(" ",end=" ")
        j=j+1
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1

    print("\n")
    i=i+1

"""

"""
      1       
    1 2 1     
  1 2 3 2 1   
1 2 3 4 3 2 1 
i=1
while i<=4:
    # for space
    j=1
    while j<=(4-i):
        print(" ",end=" ")
        j=j+1

    # for 1st triangle
    k=1
    n=1
    while k<=i:
        print(n,end=" ")
        n=n+1
        k=k+1
    # for 2nd triangle
    l=i-1
    while l>0:
        print(l,end=" ")
        l=l-1

    print("\n")
    i=i+1

"""
i=1
while i<=5:
    # 1st triange
    j=5
    n=1
    while j>0:
        print(n,end=" ")
        n=n+1
        j=j-1


    # print star
    k=1
    while k<=i-1:
        print("*",end=" ")
        k=k+1

    print("\n")
    i=i+1

   


    




    