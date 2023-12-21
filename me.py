import math as m


# defining vector class
class vec2:
    # angle input is in degrees
    def __init__(self, r, theta, x, y, deg=True):
        self.r = r
        if deg:
            self.theta = theta
        else:
            self.theta = ang.r2d(theta)
        self.rx = r * m.cos(theta)
        self.ry = r * m.sin(theta)
        self.x = x
        self.y = y


class ref:
    def __init__(self, rx, ry, x=0, y=0,deg=True):
        '''
        example usage of rx and ry. If the contact M is a 
        roller, then there is a normal force N of +N j.

        Or in case of a cantiliver beam supported to a wall,
        there is a horizontal and vertical reaction force

        And in some cases, we dont consider it, the ref can have
        a value of 0
        '''
        r = m.sqrt(rx**2 + ry**2)
        # theta = m.atan(ry/rx)
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.r = m.sqrt(rx**2 + ry**2)



class force(vec2):
    def __init__(self, r, theta, x, y, deg=True):
        super().__init__(r, theta, x, y, deg)

# defining moment class
class moment:
    
    @staticmethod
    def m2(ref: vec2, force: vec2):
        # dx, dy = force.x - ref.x, force.y - ref.y
        # M = dy * force.rx if dx != 0 else 0
        # M += dx * force.ry if dy != 0 else 0
        # return M
        dx = force.x - ref.x
        dy = force.y - ref.y
        M = 0
        if dx == 0:
            M += 0
        elif dx > 0:
            M += abs(dx) * force.ry
        else:
            M -= abs(dx) * force.ry
        
        if dy == 0:
            M += 0
        elif dy > 0:
            M += abs(dy) * force.rx
        else:
            M -= abs(dy) * force.rx
        
        return M



class inertia:
    pass




# angle class
class ang:
    @staticmethod
    def r2d(rad):
        return rad * 180 / m.pi
    
    @staticmethod
    def d2r(deg):
        return deg * m.pi / 180
    