#generator function
#it return an object
#keyword➡️yield
#calling in loop only


print(range(1,10))#special type funtion hai so this called genertor



def getcubes(limit=10):
    for i in range(1,limit+1):
        yield i**3

for val in getcubes():
    print(val)


for val in getcubes(4):
    print(val)



    