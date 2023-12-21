def q_5_50():
    import sympy as sym
    import pandas as pd
    import math as M 
    import scipy as sp

    l1 = float(input("Length of bottom rod : "))
    b1 = float(input("Breadth of top rod : "))
    l2 = float(input("Length of middle rod : "))
    b2 = float(input("Breadth of middle rod : "))
    l3 = float(input("Length of top rod : "))
    b3 = float(input("Breadth of top rod : "))

    A1 = l1*b1
    A2 = l2*b2
    A3 = l3*b3

    y1bar = b1/2
    y2bar = b2/2 + b1
    y3bar = b3/2 + b2 + b1

    A1ybar = A1*y1bar
    A2ybar = A2*y2bar
    A3ybar = A3*y3bar

    df = pd.DataFrame({'Area':[A1,A2,A3],'ybar':[y1bar,y2bar,y3bar],'Aybar':[A1ybar,A2ybar,A3ybar]})
    df.index = ['1','2','3']
    print(df)

    Ybar = (A1ybar + A2ybar + A3ybar)/(A1 + A2 + A3)
    print(f"Location of the centroid from base is : {round(Ybar,2)}")


def q_5_53():
    import pandas as pd
    import math as M

    r = float(input("Radius of the semi circle : "))
    w = float(input("Width of the cutout : "))
    h = float(input("Height of the cutout : "))

    A1 = (M.pi*r**2)/2
    A2 = w*h

    y1bar = (4*r)/(3*M.pi)
    y2bar = h/2

    A1y1bar = A1*y1bar
    A2y2bar = A2*y2bar

    df = pd.DataFrame({'Area': [A1, A2], 'ybar':[y1bar, y2bar], 'Aybar':[A1y1bar, A2y2bar]})
    df.index = ['1', '2']
    print(df)

    Ybar = (A1y1bar - A2y2bar)/(A1 - A2)
    print(f"Location of centroid on Y axis is : {round(Ybar,2)}")
    print(f"Location of centroid on X axis is : 0")

def q_A_54():
    import sympy as sym
    from sympy import simplify

    b = float(input("Length of base of the trapezoid (x b1) [x]: "))
    h = float(input("Height of the trapezoid (x h) [x]: "))
    b = float(input("Length of top of the trapezoid (x b2) [x]: "))

    b1, b2, h = sym.symbols('b1, b2, h')

    # MOI of each triangle
    Itx = 1/12 * (b1-b2)/2 * h
    Ity = 1/36*h*((b1-b2)/2)**3 + 1/2*h*((b1-b2)/2)*(b2/2 + (b1-b2)/6)**2
    # using parallel axis thorem above

    # MOI for the rectangular portion
    Irx = 1/3*b2*h**3
    Iry = 1/12*h*b2**3

    IX = Irx + 2*Itx
    IY = Iry + 2*Ity

    IX_s = simplify(IX, rational=True)
    IY_s = simplify(IY, rational=True)

    print(f"Ix : {IX_s}")
    print(f"Iy : {IY_s}")