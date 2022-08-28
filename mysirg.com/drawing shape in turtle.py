import turtle
s=turtle.getscreen()
t1=turtle.Turtle()
#⬇️from ceter blank&filled 8️⃣
#t1.circle(100)# circle radius
#t1.goto(00,-100)
#t1.dot(200) #circle diameter



#⬇️concentric circle black filled in white
#t1.circle(125)#radius
#t1.goto(0,125)
#t1.dot(62.5)#diameter


#t1.dot(130)#diameter
#t1.goto(0,-75)
#t1.circle(10)#radius




#⬇️rectangle

#1st way

#t1.goto(100,0)#left fd -------->
#t1.goto(100,50)#^^^^^^  #doubt
#t1.goto(0,50)#VVVV
#t1.goto(0,0)#

#t1.home()  #work



#2nd way

#t1.goto(100,0)
#t1.goto(100,50)
#t1.goto(100,50)
#t1.goto(0,50)
#t1.goto(0,0)



print("triangle")



t1.goto(100,0)
t1.goto(0,100)
t1.goto(-100,0)
t1.home()





turtle.done()