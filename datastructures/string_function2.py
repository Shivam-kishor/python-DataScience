#string validation function


#from curses.ascii import isalpha, isspace, isupper


value=input('enter something:')

#test
if value.isnumeric():
    print('only number',value.isnumeric())
if value.isalpha():
    print('only charachter',value.isalpha())
if value.isalnum():
    print("alpha+no.",value.isalnum())
if value.isspace():
    print('only space',value.isspace())
if value.isupper():
    print("uppercase alphabet",value.isupper())
if value.islower():
    print("lower alphabet",value.islower())   