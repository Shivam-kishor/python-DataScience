#wap ro cal total price
           #order amount>1000,discount of 3%
           #if payment from credit card then 100 rs off

order=int(input('kinte ka khana dey tumye?'))
if order>= 1000:
    #off=int(order)/int(100)int*(3)
 off=int(order/100*3)
 new_price=int(order-off)
 print('jaoo tumko 3 percent off mila',new_price)
    #if order=100:

print('wanna use credit card')

if order :
    casback=int(order-100)
    print('100 rs off hogya',casback)

