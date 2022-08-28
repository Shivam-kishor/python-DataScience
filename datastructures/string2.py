from cgi import print_form


x=chr(65)
print(x)
x=chr(2365)
print(x)

x=chr(12365)
print(x)


print('----')




y=ord('A')
print(y)

y=ord('a')
print(y)

y=ord('{')
print(y)



print('----')





print(len("amazing"))#7
print(len("world"))#5
size=len("hope")#4
print(size) 


print("---------")
a=" I'm  1 "
c='and'
b=" I am 2"
print(a+c+b)
print(-2*c*-3)

        # ⬇️6 start ⬇️0 tk jeyga     #gap hota jeyga
for i in range(6,       0,                  -1):
    print(i*'   *   ')




#for i in range(15,1,-2):
#    print((i* '😁').center(30))


    for i in range(0,11,2):
        if i==0:
            continue
        print((i*'*').center(30))

        print((i*'0').center(30))

