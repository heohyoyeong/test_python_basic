x=int(input())
a=list()
c=list()

for z in range(0,x):
    y=input()
    yy=y.split(" ")
    yy1=int(y[0])
    yy2=yy[1]
    yyy=len(yy2)
    for zz in range(0,yyy):
        for zzz in range(0,yy1):
            b=yy2[zz]
            a.append(b)
    d="".join(a)
    c.append(d)
    a=list()

cc=len(c)

for z in range(0,cc):
    print(c[z])