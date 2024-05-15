Target Pattern:
**********
**      **
* *    * *
*  *  *  *
*   **   *
*   **   *
*  *  *  *
* *    * *
**      **
**********

Code:
row = int(input("Enter number of rows:"))
for i in range (1,row+1):
    for j in range (1,row+1):
        if i==1 or i==row or j==1 or j==row or j==i or j==(row+1-i):
            print("*", end="")
        else:
            print(" ", end="")
    print("\n")
