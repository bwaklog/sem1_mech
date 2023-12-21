import math as m

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.R = m.sqrt(x**2 + y**2)


    @classmethod
    def create(cls, R, theta):
        # theta input is in degrees
        theta = Angle.deg2rad(theta)
        X = R * m.cos(theta)
        Y = R * m.sin(theta)
        return cls(X, Y)
    
    
    @classmethod
    def ref(cls, x, y):
        return cls(0.0, 0.0)


class Force:
    def __init__(self, Fx, Fy, x, y):
        self.Fx = Fx
        self.Fy = Fy
        self.x = x 
        self.y = y
        self.R = m.sqrt(Fx**2 + Fy**2)
        # theta in degrees
        self.theta = Angle.rad2deg(m.atan(Fy/Fx))

    def __repr__(self):
        return f'Fx, Fy:\t{self.Fx, self.Fy}\nx, y:\t{self.x, self.y}'

    
    @classmethod
    def create(cls, R, theta, x, y):
        # theta input is in degrees
        theta = Angle.deg2rad(theta)
        Fx = R * m.cos(theta)
        Fy = R * m.sin(theta)
        return cls(Fx, Fy, x, y)

class Angle:
    @staticmethod
    def rad2deg(rad):
        return rad * 180 / m.pi

    @staticmethod
    def deg2rad(deg):
        return (deg * m.pi)/180

class Moment:

    '''
    For calculation of moment we need to consider whether
    force contributed is clockwise w.r.t a point or ACW.
    ''' 
    @staticmethod
    def moment(ref: Vector, force: Force):
        delx = force.x - ref.x
        dely = force.y - ref.y
        M = 0
        
        # calculating M by Fx
        if dely == 0:
            M = 0 # along the axis
        elif dely > 0: # above the axis
            M += -abs(dely) * force.Fx
        else:
            M += +abs(dely) * force.Fx
        

        # calculating M by Fy
        if delx == 0: # along the axis
            M += 0
        elif delx > 0: # rhs of the axis
            M += +abs(delx) * force.Fy
        else:
            M += -abs(delx) * force.Fy
        
        
        return M 

    
    @staticmethod
    def netmoment(forcelist, ref: Vector) -> float:
        M = 0
        for force in forcelist:
            M += Moment.moment(ref, force)
        return M

if __name__=="__main__":
    O = Vector.ref(0, 0)
    F = Force.create(8, 300, 3, -0.65)
    F2 = Force.create(93.67, 137.5, 6, 9)
    forcelist = [F, F2]

    # MF = Moment.moment(O, F)
    print(Moment.netmoment(forcelist, ref=O))
