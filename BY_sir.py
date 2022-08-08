#7-august-2022
#wap to calc rate with gst above 1k items
amt=int(input("input amount"))
pm=input('payment method(credit)') 
if amt >1000:
    amt-= amt*.03 #(3/100)
if pm =='credit':
    amt -= 100
amt += amt *.18 #tax 18
print("your final amt is :",amt)