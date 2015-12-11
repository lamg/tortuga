from turtle import *
import math

def pol(l,ln,a):
    for i in range(math.ceil(360/a)):
        ln(l)
        left(a)

def tri(l):
    lt(180)
    for i in range(3):
        rt(120)
        fd(l)
    rt(180)

def flecha(l):
    pd()
    ps = pos()
    p = l/10
    fd(l-p)
    pu()
    lt(90)
    hp = p/math.sin(math.pi/3)
    fd(hp/2)
    rt(180)
    pd()
    begin_fill()
    tri(hp)
    end_fill()
    # {recta de l-p con punta triangular de altura p y base perpendicular
    # a la recta}
    pu()
    fd(hp/2)
    lt(90)
    fd(p)
    pd()

def cruz(l):
    for i in range(4):
        flecha(l)
