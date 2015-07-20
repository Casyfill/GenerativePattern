
def defineCenter(t):
    ## rotate ePoint according to t and center
    
    ## define points
    
    eX = 0.5
    eX = map(eX,0,1,150,1040-150)  # defining ePoint

    
    bPoint = PVector(0,0)  # fixed for now
    ePoint = PVector(eX,150) # fixed for now
    
    c = centerCircleCenter(bPoint, ePoint)
    
    return rotateCoord(bPoint,ePoint,c,t)

    
    
    
def centerCircleCenter(bPoint, ePoint):
    '''defines the center of the distribution'''
    
    
    avPoint = PVector((bPoint.x+ePoint.x)/2,(bPoint.y+ePoint.y)/2)
    
    vToRad = PVector(ePoint.x-avPoint.x, ePoint.y - avPoint.y)

    vToRad = rotateVector(vToRad, HALF_PI) 

    '''knowing vector to center and that center is just up to our ePoint,
    we can define center coordinates'''
    a, b = linearModel(vToRad, avPoint)
    
    centerX = ePoint.x
    centerY = a + b*ePoint.x
    
    return PVector(centerX, centerY)


def linearModel(vector, p):
        #defines a and b of linear model using vector and point
        b = vector.y/vector.x
        a = p.y - p.x*b
        return (a,b)


def rotateVector(vector, angle):
    #rotate Vector
    angle = -angle
    x = vector.x*cos(angle) - vector.y*sin(angle)
    y = vector.y*cos(angle) + vector.x*sin(angle)
    return PVector(x,y)

def angleBetweenVectors(v1,v2):
    #calculate angle between vectors
    c = (v1.x*v2.x + v1.y*v2.y)/(sqrt(sq(v1.x)+sq(v1.y))*sqrt(sq(v2.x)+sq(v2.y)))
    return acos(c)


def rotateCoord(p1,p2,c,t):
    #rotate point from to another with center point and percent t
    
    v1 = PVector(p1.x-c.x,p1.y-c.y)
    v2 = PVector(p2.x-c.x,p2.y-c.y)
    
    ang = angleBetweenVectors(v1,v2)
    newAng = ang*t
    
    vR = rotateVector(v1,newAng)
    z = angleBetweenVectors(PVector(0,1),rotateVector(vR, PI))
    
    return PVector(vR.x+c.x, vR.y + c.y, z)

def pointCyl(c, dst, ang):
    #cylindrical point constructor
    p = PVector(dst,0)
    pR = rotateVector(p, ang)
    return PVector(c.x+pR.x, c.y + pR.y)


    

    

