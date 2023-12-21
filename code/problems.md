
Using `sympy` module which is used to solve equations similar to how MATLAB solves an equation

Documentation for sympy module https://docs.sympy.org/latest/index.html
```python
pip3 install sympy
```

# Unit 1 Problems

2/50) Elements of the lower arm are shown in the figure. The mass of the forearm is 2.3 kg with center of mass at G. Determine the combined moment about the elbow pivot 0 of the weights of the forearm and the sphere. What must the biceps tension force be so that the overall moment about 0 is zero?

<img src="https://i.imgur.com/hEmTcDz.png"  width=300px/>

```python
import math as M
import sympy as sym

# moment of known forces
Mo = sum([
	2.3*9.81*(0.15*M.sin(M.radians(55))),
	3.6*9.81*(0.325)
])

T = sym.Symbol('T')
sigmaM = sym.Eq(T*0.05 - Mo, 0)

T = sym.solve(sigmaM, T)[0]
print(f'Solution for T : {T}')
```

Output
```
Solution for T : 285.001582725878
```
---
<div style="page-break-after: always"></div>

2/55) An overhead view of a door is shown. If the compressive force F acting in the coupler arm of the hydraulic door closer is 75N with the orientation shown, determine the moment of this force about the hinge axis O.

<img src="https://i.imgur.com/oLQL9MM.png" width=400 />

```python
import math as M

F = 75
theta = M.radians(20)
Fx = F*M.sin(theta)
Fy = F*M.cos(theta)

sigmaM = sum([
	0.3 * Fy,
	(25+35+38)/1000 * Fx
])

print(f'Moment of force is : {sigmaM}')
```

Output
```
Moment of force is : 23.6569320211266
```
---
<div style="page-break-after: always"></div>

2/69) A force F of magnitude 50N is exerted on the automobile parking break lever at the position x = 250mm. Replace the force by an equivalent force-couple system at the pivot point O.

<img src="https://i.imgur.com/DAk6BSU.png" width=400 />

```python
import math as M

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
```

```output
Enter value of F : 50
Angle of application : 20
Force of 50.0 with angle 110.0 deg
Moment value : 17.13972604409794
```
---
<div style="page-break-after: always"></div>

# Unit 2 Problems

3/12) The 500-kg uniform beam is subjected to the three external loads as show. Compute the reactions at the support point O. The x-y plane is vertical

<img src="https://i.imgur.com/WqxXvt2.png" width=400 />

```python
import sympy as sym
import math as M

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

print(f'Value of Ox : {result[Ox]:.2f}')
print(f'Value of Oy : {result[Oy]:.2f}')
print(f'Value of Mo : {result[Mo]:.2f}')
```

Output
```
Weight of the bar : 500
Disntace of A from O : 1.2
Force at A : 1400
Moment at B : 15000
Disntace of C from O : 4.8
Force at C : 3000
Angle made by Fc with vertical : 30
Value of Ox : 1500.00000000000
Value of Oy : 6103.08
Value of Mo : 7562.77
```
---
<div style="page-break-after: always"></div>

3/21) When on level ground, the car placed on four individual scales - one under each tyre. The scale readings are 4450 N at each front wheel and 2950 at each rear wheel. Determine the x-coordinates of the mass centre G and the mass of the car

<img src="https://i.imgur.com/AjjWFYZ.png" width=400 />

```python
Na = float(input("Scale reading for front tyres : "))
Nb = float(input("Scale reading for rear tyres : "))
d = float(input("Enter width of wheelbase (b/w D and C) : "))

W, x = sym.symbols('W, x')
sigmaFy = sym.Eq(2*Na + 2 * Nb - W*9.81, 0)
sigmaMa = sym.Eq(-W*9.81*x + 2*Nb*d, 0)
res = sym.solve([sigmaFy, sigmaMa], (W, x))

print(f'Weight of the car : {res[0][O]:.2f}kg')
print(f'Location of CM from A : {res[0][O]:.2f}mm')
```

Output
```
Scale reading for front tyres : 4490
Scale reading for rear tyres : 2950
Enter width of wheelbase (b/w D and C) : 2640
Weight of the car : 1516.82kg
Location of CM from A : 1046.77mm
```
---
<div style="page-break-after: always"></div>

2/85) Where does the resultant of the two forces act

<img src="https://i.imgur.com/XYF37ab.png" width=400 />

```python
import sympy as sym
import math as M

F1 = float(input("Force acting downards (N) : "))
d1 = float(input("Distance of downards force from A (mm) : "))
d2 = float(input("Distance of upwards force from A (mm) : "))
F2 = float(input("Force acting upwards (N) : "))

d = sym.symbols('d')

sigmaFy = sym.Eq(F1-F2, R)
sigmaMa = sym.Eq(R*d, F1*d1 - F2*d2)
res = sym.solve([sigmaFy, sigmaMa], (R, d))
print(f'Resultant of Froce: {res[0][0]:.2f}N')
print(f'Distance of resultant from A : {res[0][1]:.2f}m')
```

Output
```
Force acting downards (N) : 680
Distance of downards force from A (m) : 0.8
Force acting upwards (N) : 660
Distance of upwards force from A (m) : 0.5
Resultant of Froce: 20.00N
Distance of resultant from A : 10.70m
```
---
<div style="page-break-after: always"></div>


# Unit 3 Problems

5/50) Determine the height above the base of the centroid of the cross-sectional area of the beam. Neglect the fillets.

<img src="https://i.imgur.com/0UgBT7d.png" width=400 />

```python
import pandas as pd

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
print(f"Location of the centroid from base is : {Ybar:.2f}")
```

Output
```
Length of bottom rod : 312
Breadth of top rod : 35
Length of middle rod : 22
Breadth of middle rod : 273
Length of top rod : 156
Breadth of top rod : 35
      Area   ybar      Aybar
1  10920.0   17.5   191100.0
2   6006.0  171.5  1030029.0
3   5460.0  325.5  1777230.0
Location of the centroid from base is : 133.94
```
---
<div style="page-break-after: always"></div>

5/53) Calculate the y-coordinate of the centroid of the shaded area

<img src="https://i.imgur.com/afzoLJ7.png" width=400 />

```python
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
```

Output
```
Radius of the semi circle : 74
Width of the cutout : 64
Height of the cutout : 32
          Area       ybar          Aybar
1  8601.680686  31.406575  270149.333333
2  2048.000000  16.000000   32768.000000
Location of centroid on Y axis is : 36.
```
---
<div style="page-break-after: always"></div>

A/54) Determine the moment of inertia about the x and y axis of the trapezoidal area

<img src="https://i.imgur.com/TqxINR5.png" width=400 />

```python
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
```

Output
```
Length of base of the trapezoid (x b1) [x]: 1
Height of the trapezoid (x h) [x]: 1
Length of top of the trapezoid (x b2) [x]: 1
Ix : h*(b1 + 4*b2*h**2 - b2)/12
Iy : h*(b1**3 + b1**2*b2 + b1*b2**2 + b2**3)/48
```

---
<div style="page-break-after: always"></div>

# Unit 4 Problems

5/106) Determine the reactions at A for the cantilever beam subjected to the distributed and concentrated loads.

<img src="https://i.imgur.com/coWoxOx.png" width=500 />

```python
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
```

Output
```
Length of distributed load : 3
Distributed load (x)kN/m : 4
Concetrated load (x)kN : 2
Distance of conc. load from A (m): 4.5
Value of Ax : 0.00
Value of Ay : 8.00
Value of Moment at A : 21.00
```
---
<div style="page-break-after: always"></div>

6/9) The uniform 7-m pole has a mass of 100 kg and is supported as shown. Calculate the force P required to move the pole if the coefficient of static friction for each contact location is 0.40.

<img src="https://i.imgur.com/IFCRxrA.png" width=400 />

```python
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
```

Output
```
Mass of the pole(kg) : 100
Enter length of the rod : 7
Static Friction Coefficient : 0.4
Value of Na : 549.36
Value of Nb : 673.36
Value of P : 774.75
```
---
<div style="page-break-after: always"></div>

6/19) Determine the range of mass m2 for which the sys­tem is in equilibrium. The coefficient of static friction between the block and the incline is  $\mu_s$ = 0.25. Neglect friction associated with the pulley.


<img src="https://i.imgur.com/Y6eOfTX.png" width=400 />

```python
import sympy as sym
import math as M

N, m1, m2 = sym.symbols('N, m1, m2')
g = 9.81
theta = float(input("Enter slope incline (deg) : "))
rad = M.radians(theta)
mu_s = float(input("Coeff of static friction : "))

Fx1 = sym.Eq(+(m1+m2)*g*M.sin(rad) + mu_s*((m1+m2)*g*M.cos(rad)), m2*g)
Fx2 = sym.Eq(+(m1+m2)*g*M.sin(rad), mu_s*((m1+m2)*g*M.cos(rad)) + m2*g)

sol1 = sym.N(sym.solve(Fx1, m2)[0].coeff(m1))
sol2 = sym.N(sym.solve(Fx2, m2)[0].coeff(m1))
```

Output
```
Enter slope incline (deg) : 20
Coeff of static friction : 0.25
Range of m2 : 0.1199 <= m2 <= 1.3637
```