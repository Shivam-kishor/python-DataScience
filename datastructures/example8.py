#variable arguments-args
#keyword arguments -kwargs
def total(*values):
    t=0
    for i in values:
        if isinstance(i,(int,float)):
            t=+i
    return t
    o=total(1,2,3,4)
    print(o)

    o=total()
    print(o)

    o=total(1,2,3,4,5,5,47,9,756,44,8,64)
    print(o)
    
    o=total(1,2,3,4,'a','f'),
    print(o)