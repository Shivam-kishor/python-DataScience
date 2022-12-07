def greater_than_2(n):
    if n>2:
        return 1 or True
    else:
        return 0 or False
num=[1,2,3,19,5 ,4,-4,-6,-2]
result=list(filter(greater_than_2,num))
print(result)