#8 aug-2022
#create a fake user register system
# takle input fromb user 
# username  >4 & < 25 less char
# # email ---have @
#
#passwd ----------- confirm password 
#gender

import email


name=input('print kya name h:')
email=input('print kya email h')
passwd=input('print kya password h')
confpaswd=input('print kro confirm password yrr')
gender=input('print gender m/f/O')

if len(name)>4 &  len(name)<24:
