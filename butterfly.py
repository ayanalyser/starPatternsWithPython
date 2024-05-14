<b>Target Pattern -<b>
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *

Code:
row = int(input("Enter number of rows: "))

for i in range (1,row+1):
    print("*"*i, end="")
    x = (2*row)-(2*i)
    print(" "*x, end="")
    print("*"*i,end="\n")
    
for j in range (row,0,-1):
    print("*"*j, end="")
    y = (2*row)-(2*j)
    print(" "*y, end="")
    print("*"*j, end="\n")
