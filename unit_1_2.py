import math as M
import sympy as sym

# moment of known forces
def q1():
    Mo = sum([
        2.3*9.81*(0.15*M.sin(M.radians(55))),
        3.6*9.81*(0.325)
    ])

    T = sym.Symbol('T')
    sigmaM = sym.Eq(T*0.05 - Mo, 0)
    print(sym.solve(sigmaM, T))

def q2():
    F = 75
    theta = M.radians(20)
    Fx = F*M.sin(theta)
    Fy = F*M.cos(theta)

    sigmaM = sum([
        0.3 * Fy,
        (25+35+38)/1000 * Fx
    ])
    print(f'Moment of force is : {sigmaM}')


def q3():
    F = float(input("Enter value of F : "))
    theta = float(input("Angle of application : "))
    rad1 = M.radians(theta) # 20°
    rad2 = M.radians(theta + 15) # 25°
    rad3 = M.radians(10) # 10°

    sigmaM = sum([
        F*M.cos(rad1)*(0.1*M.cos(rad2) + 0.25*M.cos(rad3)),
        F*M.sin(rad1)*(0.1*M.sin(rad2) + 0.25*M.sin(rad3))
    ])


    # calculating force-couple system at O
    print(f'Force of {F} with angle {theta + 90} deg')
    print(f'Moment value : {sigmaM}')

def u2_q1():
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

def u2_q2():
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

def u2_q3():
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