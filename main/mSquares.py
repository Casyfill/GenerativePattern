import mb_misc as misc

class mSquare():
    '''cell of marching cubes'''
    
    def __init__(self,pos,sz, rads):
        self.pos = pos
        self.sz = sz
        
        self.points = (measurePoint(PVector(self.pos.x + sz/2, self.pos.y+sz/2) , [0]*rads),
                       measurePoint(PVector(self.pos.x + sz/2, self.pos.y-sz/2), [0]*rads),
                       measurePoint(PVector(self.pos.x - sz/2, self.pos.y-sz/2), [0]*rads),
                       measurePoint(PVector(self.pos.x - sz/2, self.pos.y+sz/2), [0]*rads))  # clockwise. Z is for dist's

        self.pD = [[False,False,False,False] for x in xrange(rads)]
        self.status = [False ]*rads                                         # if border
        
    
    def measure(self, balls, j):
        for i, p in enumerate(self.points):
            d = 0
            for ball in balls:
                d+= pow(ball.rads[j],4)/(sq(p.pos.x - ball.pos.x) + sq(p.pos.y - ball.pos.y))
            
            p.mArray[j] = d
            if d >1:
                self.pD[j][i] = True
            else:
                self.pD[j][i] = False
        
        self.statusCheck(j)
    
    def measure2(self, balls, j):
        for i, p in enumerate(self.points):
            d = 0
            for ball in balls:
                d+= pow(ball.rads[j]/(dist(ball.pos.x, ball.pos.y, p.pos.x, p.pos.y)), 7)
            
            p.mArray[j] = d
            if d >1:
                self.pD[j][i] = True
            else:
                self.pD[j][i] = False
        self.statusCheck(j)
    
    def statusCheck(self,j):
        if sum(self.pD[j]) in (1,2,3):
            self.status[j] = True
        else:
            self.status[j] = False
   
    
    def vizCorners(self,rads):
        '''viz cornerPoints'''
        rectMode(CENTER)
        noStroke()
        fill('#02F530')
    
        if self.status:
            for i, p in enumerate(self.points):
                if any([self.pD[x][i]for x in xrange(rads)]):
                    rect(p.pos.x,p.pos.y, 2,2)
                    
                else:
                    pass
        
    def vizGrid(self):
        stroke('#3F8B69')
        rectMode(CENTER)
        '''draw Grid'''
        if any(self.status):
            fill('#618983')
        else:
            noFill()
        rect(self.pos.x, self.pos.y, self.sz,self.sz)

          
    
    def vizLines(self,rads):
        '''draw metaball borders'''
        for j in xrange(rads):
            if self.status[j]:
                self.lineDraw(j)
   
        
    def lineDraw(self,j):
        stroke(255,0,0)
        #strokeWeight(0.5)
        rd = 4
        
        s =  sum(self.pD[j]) # number of active corners
        if  s == 1:
            # corner
            i = misc.findIndices(self.pD[j], True)[0]
            
            if i==3:
                si = 0
            else:
                si = i+1
            
            p1  =  misc.roundPoint(calcDelta(self.points[i-1], self.points[i],j))
            p2  =  misc.roundPoint(calcDelta(self.points[i], self.points[si],j))
            
            line(p1.x, p1.y, p2.x, p2.y)
            ellipse(p1.x, p1.y, rd,rd)
            ellipse(p2.x, p2.y, rd,rd)
            
            
        elif s ==2:
            # side or diag
            Is = findIndices(self.pD[j], True)
            
            
            if (0 in Is and 3 in Is) or (1 in Is and 2 in Is):
                #horizont.
                p1  =  misc.roundPoint(calcDelta(self.points[0], self.points[1],j))
                p2  =  misc.roundPoint(calcDelta(self.points[2], self.points[3],j))
                line(p1.x, p1.y, p2.x, p2.y)
                ellipse(p1.x, p1.y, rd,rd)
                ellipse(p2.x, p2.y, rd,rd)
            elif (0 in Is and 1 in Is) or (2 in Is and 3 in Is):
                #vert
                p1  =  misc.roundPoint(calcDelta(self.points[1], self.points[2],j))
                p2  =  misc.roundPoint(calcDelta(self.points[3], self.points[0],j))
                line(p1.x, p1.y, p2.x, p2.y)
                ellipse(p1.x, p1.y, rd,rd)
                ellipse(p2.x, p2.y, rd,rd)
            else:
                if 0 in Is:
                    p11  =   misc.roundPoint(calcDelta(self.points[2], self.points[3],j))
                    p12  =   misc.roundPoint(calcDelta(self.points[3], self.points[0],j))
                    
                    p21  =   misc.roundPoint(calcDelta(self.points[0], self.points[1],j))
                    p22  =  misc.roundPoint(calcDelta(self.points[1], self.points[2],j))
                    
                else:
                    p11  =  misc.roundPoint(calcDelta(self.points[3], self.points[0],j))
                    p12  =  misc.roundPoint(calcDelta(self.points[0], self.points[1],j))
        
                    p21  =  misc.roundPoint(calcDelta(self.points[1], self.points[2],j))
                    p22  =  misc.roundPoint(calcDelta(self.points[2], self.points[3],j))
                    
                line(p11.x, p11.y, p12.x, p12.y)
                line(p21.x, p21.y, p22.x, p22.y)
                ellipse(p11.x, p11.y, rd,rd)
                ellipse(p12.x, p12.y, rd,rd)
                ellipse(p21.x, p21.y, rd,rd)
                ellipse(p22.x, p22.y, rd,rd)
            
        elif s ==3:
            i = [x for x in (0,1,2,3) if x not in misc.findIndices(self.pD[j], True)][0]
            
            if i==3:
                si = 0
            else:
                si = i+1
            
            p1  =  misc.roundPoint(calcDelta(self.points[i-1], self.points[i],j))
            p2  =  misc.roundPoint(calcDelta(self.points[i], self.points[si],j))
            
            line(p1.x, p1.y, p2.x, p2.y)
            ellipse(p1.x, p1.y, rd,rd)
            ellipse(p2.x, p2.y, rd,rd)
            
                    
    def getLines(self,j):
        '''get points on the border of cell'''
        s =  sum(self.pD[j])
        if  s == 1:
            # corner
            i = misc.findIndices(self.pD[j], True)[0]
            
            if i==3:
                si = 0
            else:
                si = i+1
            
            p1  =  misc.calcDelta(self.points[i-1], self.points[i],j)
            p2  =  misc.calcDelta(self.points[i], self.points[si],j)
            
                
            
        elif s ==2:
            # side or diag
            Is = misc.findIndices(self.pD[j], True)
            
            
            if (0 in Is and 3 in Is) or (1 in Is and 2 in Is):
                #horizont.
                p1  =  misc.calcDelta(self.points[0], self.points[1],j)
                p2  =  misc.calcDelta(self.points[2], self.points[3],j)
            
            elif (0 in Is and 1 in Is) or (2 in Is and 3 in Is):
                #vert
                p1  =  misc.calcDelta(self.points[1], self.points[2],j)
                p2  =  misc.calcDelta(self.points[3], self.points[0],j)
                
            else:
                if 0 in Is:
                    p11  =  misc.roundPoint(misc.calcDelta(self.points[2], self.points[3],j))
                    p12  =  misc.roundPoint(misc.calcDelta(self.points[3], self.points[0],j))
                    
                    
                    p21  =  misc.roundPoint(misc.calcDelta(self.points[0], self.points[1],j))
                    p22  =  misc.roundPoint(misc.calcDelta(self.points[1], self.points[2],j))
                    
                    x = misc.vectorLine(p11,p12)
                    y = misc.vectorLine(p21,p22)
                    
                    return (x,y)
                
                else:
                    p1  =  misc.calcDelta(self.points[3], self.points[0],j)
                    p2  =  misc.calcDelta(self.points[0], self.points[1],j)
            
    
        elif s ==3:
            i = [x for x in (0,1,2,3) if x not in misc.findIndices(self.pD[j], True)][0]
            
            if i==3:
                si = 0
            else:
                si = i+1
            
            p1  =  misc.calcDelta(self.points[i-1], self.points[i],j)
            p2  =  misc.calcDelta(self.points[i], self.points[si],j)
            
        return misc.vectorLine(misc.roundPoint(p1),misc.roundPoint(p2))     
        
        

                
            

def SquareGrid(sp, w, h, sz, rads):
    '''Generate grid of squares all over the canves '''
    squares = []
    
    xs = ceil(w/sz)+1
    ys = ceil(h/sz)+1
    
    for x in xrange(xs):
        for y in xrange(ys):
            squares.append(mSquare(PVector(sp.x + (sz/2+x*sz), sp.y + (sz/2 + y*sz)), sz, rads))
    return squares
           
def defineLines(balls, Squares, rads):
    ''' return an array of line arrays, one for each radius'''
    lines = []
    stroke(0,255,0)

    for j in xrange(rads):
        lines.append([])
        for square in Squares:
            #square.measure(balls, j)
            square.measure2(balls, j)
            if square.status[j]:
                l = square.getLines(j)
                if type(l)== tuple:
                    lines[j].extend(l) # there is a rare case where there are 2 lines of the same rad in one rect
                else:
                    lines[j].append(l)
    return lines


class measurePoint():
    ''' point with measurments array'''
    def __init__(self,pos, mArray):
        self.pos = pos
        self.mArray = mArray

