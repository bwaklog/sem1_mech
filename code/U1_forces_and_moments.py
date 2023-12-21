import math as M
import sympy as sym

# moment of known forces
def q_2_50():
    Mo = sum([
        2.3*9.81*(0.15*M.sin(M.radians(55))),
        3.6*9.81*(0.325)
    ])

    T = sym.Symbol('T')
    sigmaM = sym.Eq(T*0.05 - Mo, 0)
    print(sym.solve(sigmaM, T))

def q_2_55():
    F = 75
    theta = M.radians(20)
    Fx = F*M.sin(theta)
    Fy = F*M.cos(theta)

    sigmaM = sum([
        0.3 * Fy,
        (25+35+38)/1000 * Fx
    ])
    print(f'Moment of force is : {sigmaM}')


def q_2_69():
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