def q_5_106():
    import sympy as sym
    import math as M 

    dll = float(input("Length of distributed load : "))
    dlx = 2*dll/3
    dl = float(input("Distributed load (x)kN/m : "))
    Req = 1/2 * dll * dl

    cl = float(input("Concetrated load (x)kN : "))
    clx = float(input("Distance of conc. load from A (m): "))

    Ax, Ay, Ma = sym.symbols('Ax, Ay, Ma')

    sigmaFx = sym.Eq(Ax, 0)
    sigmaFy = sym.Eq(Ay - Req - cl, 0)
    sigmaMa = sym.Eq(Ma - Req * dlx - cl * clx, 0)

    res = sym.solve([sigmaFx, sigmaFy, sigmaMa], (Ax, Ay, Ma))
    print(f"Value of Ax : {res[Ax]:.2f}")
    print(f"Value of Ay : {res[Ay]:.2f}")
    print(f"Value of Moment at A : {res[Ma]:.2f}")


def q_6_9():
    import sympy as sym
    import math as M 

    W = float(input("Mass of the pole(kg) : "))
    l = float(input("Enter length of the rod : "))
    if l <= M.sqrt(3**2+4**2):
        raise ValueError

    mu_s = float(input("Static Friction Coefficient : "))

    Na, Nb, P = sym.symbols('Na, Nb, P')

    sigmaMb = sym.Eq((W*9.81)*(4/5)*(l/2) - 5*Na, 0)
    sigmaFy = sym.Eq(Nb - (W*9.81) + (4/5)*(Na) - mu_s*(Na)*(3/5), 0)
    sigmaFx = sym.Eq(-P + mu_s*Nb + Na*(3/5) + 0.4*(Na)*(4/5) , 0)

    res = sym.solve([sigmaMb, sigmaFy, sigmaFx], (Na, Nb, P))
    print(f"Value of Na : {res[Na]:.2f}")
    print(f"Value of Nb : {res[Nb]:.2f}")
    print(f"Value of P : {res[P]:.2f}")

def q_6_19():
    import sympy as sym
    import math as M

    N, m1, m2 = sym.symbols('N, m1, m2')
    g = 9.81
    theta = float(input("Enter slope incline (deg) : "))
    rad = M.radians(theta)
    mu_s = float(input("Coeff of static friction : "))

    # same for both cases
    # sigmaFx = sym.Eq( - (m1+m2)*9.81*M.cos(rad), 0)

    # Fy = sym.Eq(N, (m1+m2)*g*M.cos(rad))

    Fx1 = sym.Eq(+(m1+m2)*g*M.sin(rad) + mu_s*((m1+m2)*g*M.cos(rad)), m2*g)
    Fx2 = sym.Eq(+(m1+m2)*g*M.sin(rad), mu_s*((m1+m2)*g*M.cos(rad)) + m2*g)

    sol1 = sym.N(sym.solve(Fx1, m2)[0].coeff(m1))
    sol2 = sym.N(sym.solve(Fx2, m2)[0].coeff(m1))

    print(f'Range of m2 : {sol2:.4f} <= m2 <= {sol1:.4f}')