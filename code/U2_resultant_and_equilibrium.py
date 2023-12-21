def u_3_12():
    import sympy as sym
    Ox, Oy, Mo = sym.symbols('Ox, Oy, Mo')

    W = float(input("Weight of the bar : "))
    da = float(input("Disntace of A from O : "))
    Fa = float(input("Force at A : "))
    Mb = float(input("Moment at B : "))
    dc = float(input("Disntace of C from O : "))
    Fc = float(input("Force at C : "))
    theta = float(input("Angle made by Fc with vertical : "))
    rad = M.radians(theta)

    # equation for sigma Fx = 0 for a body in equlibrium
    eq1 = sym.Eq(Ox - Fc*M.sin(rad), 0)
    # equation for sigma Fy in eqb.
    eq2 = sym.Eq(Oy + Fa - W*9.81 - Fc * M.cos(rad), 0)

    # moment in equlibrium
    eq3 = sym.Eq(Mo+ Fa*da - W*9.81*2.4 + Mb - Fc*M.cos(rad)*dc, 0)

    result = sym.solve([eq1, eq2, eq3], (Ox, Oy, Mo))

    print(f'Value of Ox : {round(result[Ox], 2)}')
    print(f'Value of Oy : {round(result[Oy], 2)}')
    print(f'Value of Mo : {round(result[Mo], 2)}')

def q_3_21():
    import sympy as sym
    import math as M

    Na = float(input("Scale reading for front tyres : "))
    Nb = float(input("Scale reading for rear tyres : "))
    d = float(input("Enter width of wheelbase (b/w D and C) : "))

    W, x = sym.symbols('W, x')
    sigmaFy = sym.Eq(2*Na + 2 * Nb - W*9.81, 0)
    sigmaMa = sym.Eq(-W*9.81*x + 2*Nb*d, 0)
    res = sym.solve([sigmaFy, sigmaMa], (W, x))

    print(f'Weight of the car : {round(res[0][0], 2)}kg')
    print(f'Location of CM from A : {round(res[0][1], 2)}mm')

def u_3_85():
    import sympy as sym
    import math as M

    F1 = float(input("Force acting downards (N) : "))
    d1 = float(input("Distance of downards force from A (m) : "))
    F2 = float(input("Force acting upwards (N) : "))
    d2 = float(input("Distance of upwards force from A (m) : "))

    R, d = sym.symbols('R, d')

    sigmaFy = sym.Eq(F1-F2, R)
    sigmaMa = sym.Eq(R*d, F1*d1 - F2*d2)
    res = sym.solve([sigmaFy, sigmaMa], (R, d))
    print(f'Resultant of Froce: {round(res[0][0], 2)}N')
    print(f'Distance of resultant from A : {round(res[0][1], 2)}m')