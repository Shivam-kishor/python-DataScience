prime_no=int (input("to check input a number"))
for i in range(0,prime_no):
    if i%prime_no==0:
        print("this is prime")
        break
    else:
        print("this isnt a prime no")