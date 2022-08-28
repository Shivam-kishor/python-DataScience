#7-august-2022
#wap to calc rate with gst if price >= 1k items
total_cost=float (input('total cost is :'))
print("hello ,sir This➡️",{total_cost},'⬅️'"$ cost for ur things :")
mode_of_payment=('upi','credit card','debit card') #tuple()
print("How would U wann TO Prefer to Pay:",mode_of_payment)
mode_of_payment1=input((mode_of_payment))
if total_cost>=1000:
    amt=float(total_cost/100*3)
    new_amount_to_pay=total_cost-amt
    print("you got 3% discount CONGRATULATION:",new_amount_to_pay)
    gst = total_cost*.18
    with_gst=gst+new_amount_to_pay
    print('with GST include 18%',with_gst)
if total_cost<1000:
    print("pay",total_cost)
    gst = total_cost*.18
    with_gst=gst+total_cost
    print('with GST include 18%',with_gst)
print("THANKYOU HOPE WE SERVE AGAIN")