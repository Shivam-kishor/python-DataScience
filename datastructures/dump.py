#fibonacci series via user input

n1=0  #indexing
n2=1  #indexing
sum=0
fib=int(input("enter number to find fibnoacci series"))
if fib<=0:
    print("invalid must be enter greater than 0")
else:
    for i in range(0,fib):
        print(sum,end=" , ")
        n1=n2
        n2=sum
        sum=n1+n2w