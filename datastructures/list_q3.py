from pyexpat.errors import XML_ERROR_SUSPENDED


x=[3,65,3,4,6,76,3,25,4,7,8,6,35,75,865,8,5,547,635,6,8765,75,68,78,6,84,68,768,6]

x_even=[]
x_odd=[]
no_greater_8_=[]

for i in x:
    if i%2==0:
        x_even.append(i)
    else:
        x_odd.append(i)
    #if i>8:
        #print(no_greater_8_.append(i))


xg8=[]
for i in  x:
    if i > 8:
        xg8.append(i)     

print("list h [x]",x)
print("EVEN ➡️",x_even)
print("ODD ➡️",x_odd)
print(xg8)
#print("no grter 8 ➡️",no_greater_8_)