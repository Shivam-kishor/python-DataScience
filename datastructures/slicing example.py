name='shivam kishor'
fname=name[:5]
lname=name[-5:]
mname=[::-8]
print(fname,mname,lname)

#reversed
rev_name=name[::-1]


#middle name revrsed

mname_rev= name[6:-8][::-1]
print(mname_rev)

#every even index number
even_name=name[::2]

#every odd index charchter
odd_name=name[1:2]
print(even_name,odd_name)