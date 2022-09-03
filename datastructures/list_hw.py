#wap to crate a list from user of n elmnt.if the user emters a duplicate value
#dont do  add  it to list anmd warn the user about their  mistAKE

#wap to create a list   and then replace then replace all value grrater than 5,by0
# #
# wap to ctreate a list and that comtain 5 small sublist of 3 items each (nested list)
# #take the input from user to create their nested list.

blank_lis=[]

#doubt particular n element to be created how? from user
in_lis=(input('enter list want to create:\n '))

for i in (in_lis) :
    blank_lis.append(i)
print(blank_lis)


for j in range(in_lis):
    blank_lis.append(j)
print(blank_lis)
if blank_lis==in_lis:
    print("already exist")