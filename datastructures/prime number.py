#note➡️ 1 is nor prime neither composite no.
#459 is not prime
#437 is no prime (437/19=23)
#443 yes
# 473 no prime (11 s cut jyga)

#prime no is no divided by itself and 1
#first prime is 2(even number)  & only prime number 
#5 is only prime number unit digit end with 5 later after not any digit ending with 5
#1 to 100 prime number is =25
#1 to 1000 prime number is =168
#  ⬇️rule to check⬇️
# number ending with 2,4,6,8,0 will not be prime number as due to it divided by 2😁
#sum of no divided by 3 then=not a prime no.
#            OR
#sum of no.is not divided by 3 then=chanches of a prime no.
# if number is divided by 2 and 3 then will aslo divided by 6 too.
#then divide by 7 if tooo not divisible by 7
#then less than that no by1  && add 1 ... divide by 6  if both divided then this is prime no

#check 11 divisibility { sum of (odd) place digits - sum of (even) places digits= multiple of 11 or 0

#             ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️                ⬇️ 




#composite number  no having itself as well as 1 along other factor term composite number
#first composite no is 4
#1 to 100 composite number={ (100-prime=75-1)= 74 }
#1 to 1000 composite number={  831 }


prime_no=[]
for num in range(2,100):
    for i in range(2,num):
        if num%i==0:
            break   
    else: 
        prime_no.append(num)
for p in prime_no:
    print(p,end=',')
    
    