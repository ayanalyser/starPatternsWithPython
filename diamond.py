Target Pattern: 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

Code:
row = int(input("Enter number of rows:"))
for i in range (0,row):
     print(" "*(row-i-1), end="")
     print("* "*(i+1))

for i in range (row, 1, -1):
    print(" "*(row-i+1), end="")
    print("* "*(i-1))
