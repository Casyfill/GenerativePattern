def findIndices(l, el):
    '''returns a list of indicies for each occurance of el in the list''' 
    return [i for i, j in enumerate(l) if j == el]

def calcDelta(p1,p2, j):
    '''calcinterpolation'''
    if p1.pos.x == p2.pos.x:
        # vertical
        c = p1.pos.y + (p2.pos.y - p1.pos.y)*(1 - p1.mArray[j])/(p2.mArray[j]-p1.mArray[j])
        return PVector(p1.pos.x, c)
        
    elif p1.pos.y == p1.pos.y:
        #horisontal
        c = p1.pos.x + (p2.pos.x - p1.pos.x)*(1 - p1.mArray[j])/(p2.mArray[j]-p1.mArray[j])
        
        return PVector(c, p1.pos.y)
    
def meanPoint(p1,p2):
    '''calculate average point between two'''
    return PVector((p1.x+p2.x)/2,(p1.y+p2.y)/2)



def drawCurves2(c, aes):
    strokeWeight(aes['strokeWeight'])
    stroke(aes['color'])
    if len(c)>=2:
        drawBlob(c)


def drawFills(c, aes):
    '''draw curves trhough all marching points'''
    if len(c) >=2:
        noStroke()
        fill(aes['color'])    
        drawBlob(c)

def drawLine(c):
    stroke(255)
    for i in xrange(len(c)-1):
        line(c[i].x, c[i].y, c[i+1].x, c[i+1].y)
        

class vectorLine():
    '''mainly a vector of two points'''
    def __init__(self,p1,p2):
        self.points = [p1,p2]
    
    def viz(self):
        stroke(0,255,0)
        line(self.points[0].x,self.points[0].y,self.points[1].x,self.points[1].y)
    
    def __str__(self):
        return str(self.points[0]) + ', ' + str(self.points[1])
    
    def rvrs(self):
        #replace start and end of the line
        return vectorLine(self.points[1], self.points[0])
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)
    
        
def roundPoint(p):
    return PVector(round(p.x), round(p.y))    


class ball():
    
    def __init__(self, pos, dir, rads):
        self.pos = pos # position
        self.dir = dir # direction
        self.rads = rads # radius
#         noFill()
#         stroke(255,0,0)
#         ellipse(self.pos.x, self.pos.y, rads[-1], rads[-1])
            
    
    def update(self):
        self.pos.x+=self.dir.x
        self.pos.y+=self.dir.y
        
        #self.viz()
        
        if 0>self.pos.x or self.pos.x>width:
            self.dir.x*=-1
            
        if 0>self.pos.y or self.pos.y>height:
            self.dir.y*=-1
    
    def viz(self):
        '''visualize ball'''
        fill(255,255,255,100)
        noStroke()
        m = self.rads[-1]
        ellipse(self.pos.x, self.pos.y, m, m)

def chP(p1,p2, t):
        if dist(p1.x,p1.y,p2.x, p2.y) <=t:
            return True
        else:
            return False


def cntrNew(lines, t):
    '''group lines into countur sequenses'''
    t =2 # toleranse is no more than 2 pixls
    
    s, e = lines[0].points[0], lines[0].points[1]
    
    sqnss = [[s, e]] # initial sequence
    lines.remove(lines[0])
    lines+=[l.rvrs() for l in lines] 
    
    while len(lines[:])>0:
        f= True
        while f:
            f = False
            sdLines = sorted(lines[:], key= lambda l: dist(e.x, e.y, l.points[0].x, l.points[0].y))
            el = sdLines[0]
            
            if chP(e,el.points[0], t):
                #print 'added to the end'
                e = el.points[1]
                sqnss[-1]= sqnss[-1] + [e]
                f = True        
                
            elif chP(s,el.points[0], t):
                #print 'added to the start'
                s = el.points[1]
                sqnss[-1]= [s] + sqnss[-1]
                f = True
           
            if f:
                lines.remove(el)
                for el2 in lines:
                    if el2 == el.rvrs():
                        lines.remove(el2)
                #print sqnss[-1], '|', str(el), '|',[str(l) for l in lines]
            if len(lines)==0:
                f=False
        
        if len(lines)>0:

            el = lines[0]
            e = el.points[1]
            s = el.points[0]
            
            sqnss.append([s,e])
            lines.remove(el)
            for el1 in lines: 
                if el1==el.rvrs():
                    lines.remove(el1)
            #print 'new One!'
            #print sqnss[-1], '|', [str(l) for l in lines]
        
    return sqnss

   
def drawBlob(ps): 
    '''draw line'''
    if dist(ps[0].x, ps[0].y, ps[-1].x, ps[-1].y)<20:
        beginShape()
        ps = ps[1:]
        
        z = averageVector(ps[-1], ps[0])
        
        curveVertex(ps[-1].x, ps[-1].y)
        curveVertex(z.x, z.y)
        
        for p in ps:
            curveVertex(p.x, p.y)
        
        curveVertex(z.x, z.y)
        curveVertex(ps[0].x, ps[0].y)
        endShape()
        
        
    else:
        noFill()
        beginShape()
        
        curveVertex(ps[0].x, ps[0].y)
        for p in ps:
            curveVertex(p.x, p.y)
    
        curveVertex(ps[-1].x, ps[-1].y)

        endShape()

def averageVector(p1,p2):
    return PVector((p1.x+p2.x)/2, (p1.y+p2.y)/2) 
          

def toPoint(p1,p2, t):
    '''move p1 to p2 on t percents where 1 = 100%'''
    return PVector(p1.x + t*(p2.x-p1.x), p1.y + t*(p2.y-p1.y))
    
      
def smoothCurve(ps, t):
    
    newP = []
    newP.append(ps[0])
    for i in xrange(1,len(ps)-1):
        if not chP(ps[i-1], ps[i], 7):
            newP.append(ps[i])
    newP.append(ps[-1])
            
    
    for i in xrange(1,len(newP)-1):
        z = averageVector(newP[i-1],newP[i+1])
        newP[i] = toPoint(newP[i], z, t)
    
    return newP    
