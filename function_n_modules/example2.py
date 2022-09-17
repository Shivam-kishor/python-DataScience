#return value
def area():
    l=int (input('enter the length:'))
    b=int (input('enter the breadth:'))
    return l*b


def minmax():
    x=[23,2,4,5,6,5,31]
    return min(x),max(x)  #returning more than 1 value

    #calling
'''
#direct calling    
print("area=>",area())


#by new variablee
ans=area() 
print("area->",ans)

ans=area()+area()-area()
print('total area->',ans)
'''
values=minmax()
x,y=minmax()

print(minmax())

print(values)

print(x,y)

