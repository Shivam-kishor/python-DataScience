#8 aug-2022
#create a fake user register system
# takle input fromb user 
# username  >4 & < 25 less char
# # email ---have @
#
#passwd ----------- confirm password 
#gender

#ladder if else
#or called nested loop


name=input('print kya name h:')
email=input('print kya email h:')
passwd=input('print kya password h')
confpaswd=input('print kro confirm password yrr:')
gender=input('print gender m/f/O:')
print("-------------------------------------------")
if (len(name)>4 and len(name)<24) :
    print(name)
    
    if '@' in email:
        print(email)
        if confpaswd==passwd:

                print("passwd matched")
        else: 
            print('passwd does not macthes')
    else:
        print('error @ is MUST include ',email)
else:

 print("error ur name is must be < than 4 and >24" ,name)


print(gender)