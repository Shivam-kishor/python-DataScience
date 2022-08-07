amt=int(input("input amount"))
pm=input('payment meyhod(credit)') 
if amt >1000:
    amt-= amt*.03 #(3/1000)
if pm =='credit':
    amt -= 100
amt += amt *.18 #tax 18
print("your final amt is :",amt)