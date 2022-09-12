'''lambda a,b:a+b

#<function_main_.<lambda>(a,b)>




adder=lambda a,b:a+b
adder(69,225)



def exp(power):
    return lambda l:[a**power for a in l]
four =exp(4)
four([2,4,6,8,10])
'''
#from re import X


'''

x=[1,2,4,5,6,7,8 ,9]
outp=list(map(lambda i:i**2,x))
print(outp) #lazy object aya but list m nhi aya na genrete hua
#so convert to list,tuppe,etc
'''



x=[1,4,6,6,5,34,46]
y=[5,5,6,7,5,3,2,7,5]

#z3=tuple(lambda i:i>3,x)
#print (z3 )

y3=list (filter(lambda i:i>3,x))
print(y3)


name=['raj singh','raj hismesh','raj thakur','vikra oandey','rajan singh',]
name_singh_op=list(filter(lambda n: n.endswith('singh'),name))
print(name_singh_op)

xy=list(map(lambda a,b:a+b,x,y))
print(xy)



#generator function
#it return an object
#keyword➡️yield
#calling in loop only


print(range(1,10))#special type funtion hai so this called genertor