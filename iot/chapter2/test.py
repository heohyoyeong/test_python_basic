# def findmin(*ints):
#     b=[]
#     for a in ints:
#         b+=str(a)
#     return (b)
#
# min=findmin(2,3,4,5,6,-7)
#
# print(min)


def findmin(*ints):
    b=999999999999
    for a in ints:
        if b>=a:
            b=a
        else:
            pass
    return(b)


min=findmin(2,3,4,5,1,6,-8,7)

print(min)