#prime ==>😁 1%==0 && itself==-0    


naval=int(input("enter a no:"))

if(naval==1):
    print("prime hai if wala➡️")

    #indentation
for i in range(2,naval+1):
    if(naval %i==0 ):
        print("prime nhi h 😁 for wala")
        break
    else:
        print("prime h 2nd baar loop wala➡️")
        break







else:
    print("prime nhi hai 😁else wala")
