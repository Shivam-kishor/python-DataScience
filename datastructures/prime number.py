#
prime_no=[]
for num in range(2,100):
    for i in range(2,num):
        if num%i==0:
            break   
    else: 
        prime_no.append(num)
for p in prime_no:
    print(p,end=',')
    
    