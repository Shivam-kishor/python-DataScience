data="" #global variable

def data_appender(aaaaaaaaaaaaaaaaaaaaaa):
    global data #this line tell data_appender that we have a global var data
    if len(aaaaaaaaaaaaaaaaaaaaaa)>0:
        data+=aaaaaaaaaaaaaaaaaaaaaa


#call
data_appender('hello ')
data_appender(' world')
data_appender(' this is a simple function')
data_appender(' \n pehle istemal kre phir vishwas kre')


print(data)