#prime no via function  divided by 1%==0 || itself %=00 
user=int(input("enter a number to check"))
#i=1
def prime():
    if(user ==1):
        print(" prime hai without function๐ ")
        for i in range(2,user+1):
            if(user %i==0):
                print("this is prime ,function wala๐๐")

            else:
                print("nhi hai prime function wala๐๐")

    else:
        print("NHI HAI prime ๐ without function")


prime()
