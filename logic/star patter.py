#star=input("enter pattern row and colum")

for x in range(10,1,-1):
    for y in range(x,x-1):
        print("*",end=" ")
    print()             #gap but star didnt print
    


"""
for row in range(1,11):
    for column in range(row,row+1):
        print(" * ",end=" ")
    print( )"""