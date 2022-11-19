sub1=int(input("entyer the first subject number"))
sub2=int(input("entyer the seocnd subject number"))
sub3=int(input("entyer the third subject number"))
sub4=int(input("entyer the fourth subject number"))

total=sub1+sub2+sub3+sub4
print(total)

per=(total/400)*100

if(per>=80):
	print("the gtrade is A")

elif(per>=65 and per<=80):
	print("the gtrade is C")

elif(per<=65 and per>=33):
	print("the grade is C")
else:
	print("collage a piche jata hai")
	