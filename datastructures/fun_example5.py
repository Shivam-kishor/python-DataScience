#10 sep/2022
#default parameter
#from re import A


#def default(a=50,b=100):
 #   return a+b
#print(default())#op=150


def triangle_area(b,h=1):
    return 1/2*b*h

print(triangle_area(10))
print(triangle_area(5,3))
print(triangle_area(b=5))
print(triangle_area(b=8,h=6))


def read(filepath=None):
    if filepath:
        with open(filepath)as f:
            return f.read()
    else:
        return '⚠️pls provide a path name⚠️'

print(read('g1.py'))
print(read())


'''
default_function()
print(default_function())

default_function(a=99)
print(default_function(a))'''