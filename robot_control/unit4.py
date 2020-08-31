def myFun():
    print("test")

myFun()


def myFun2():
    print("test2")

myFun2()

def add(a,b):
    r = a+b
    print(r)
    return r

add(1,2)

def add2(a=None, b=None):
    if( a == None ):
        a = 2
    if( b == None ):
        b = 3
    r = a+b
    r = [ r, a, b]
    print(r)
    return r
add2(1.1)