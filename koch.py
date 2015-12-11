import turtle

def thue_morse(n):
    assert n >= 0 
    a = [False]
    while n != 0:
        b = []
        for i in a:
            b.append(not i)
        a = a+b
        n-=1
    return a

def koch(n):
    assert n >= 0
    tm = thue_morse(n)
    for i in tm:
        if i:
            turtle.lt(60)
        else:
            turtle.fd(1)
        
