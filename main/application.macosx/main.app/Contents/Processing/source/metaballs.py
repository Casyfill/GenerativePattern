add_library('isolines')
import isolines

finder = isolines.Isolines(this, 1040, 300)

def renderMetaballs1(balls, logics,state):
    '''render slow metaball image'''
    from colorGradients import Gradientr
    bounds = state['bounds']
    h = 300
    
    s = millis()
    
    
    
    G = Gradientr()
    img = createImage(width,h, ALPHA)
    
    
    numBalls = len(balls)
    
    
    
    
    mD = 0
    for x in xrange(width):
        for y in xrange(h):
            
            ds = 0.0
            
            for ball in balls:
                #r = 0.5*ball.radius*ball.density*state['aSize']
                d = sq(ball.radius/dist(x,y, ball.position.x, ball.position.y)) # distance to pixel
                ds+=d
                
                #col += ball.radius / d   #primitive additional calculation
            
            #print sum(ds)
            D = ds
            if D > mD:
                mD = D
            
            col = logics(D, state, G)
                    
                
            # (lerpColor(color(0,0,0),color(255,255,255),col ))
            img.pixels[x+y*width] = col
    print 'mD:', mD
    
    e = millis()
    print e-s
    
    
    img.updatePixels()
    image(img, 0, 0)
    
    #for ball in balls:
    #    ball.crossViz(state)
    
    
def draw1(D, state, G):
    '''logics1'''
    
    i = 1
    wd = 0.2
    col = color(0)
    
    bounds =  state['bounds']
    
    
    colrScheme = state['color']
    #print 'cS',colrScheme
    
    c = remap(D,0,2000000,1.0,0.0)
    col=G.gradientAgent(c,colrScheme)
    
    for b in xrange(bounds):
        #p = remap(i,80.0,500.0,0.0,1.0)
        wd-= i*0.02
        
        j = remap(float(b),0,bounds,0.3,5.0)
        
        if j<D<j+wd:
            c = remap(float(b),0,bounds,0.0,1.0)
            if state['rColor']: 
                c = 1-c
            col=G.gradientAgent(c,colrScheme)
            
        
    #print 'col:',col
            
    return col

    
def draw2(D, state, G):
    '''logics2'''
    
    i = 1
    wd = 0.2
    col = color(0)
    
    bounds =  state['bounds']
    
    for x in xrange(bounds):
        jx = 1.0- float(x)/bounds
        
        if D > 0.3 + 0.3*sq(x):
            col=G.gradientAgent(jx,state['color'])    
            
    return col

def remap(i, s1,s2, e1,e2):
    f = (i-s1)/(s2-s1)
    return(e1 + f*(e2-e1))


def delocateOne(agent, plane, t):
    from geomLogics import rotateVector

    
    angle = plane.z + (HALF_PI/7)*t
    agent.position = rotateVector(agent.position, angle)
        
    agent.position.x += plane.x
    agent.position.y += plane.y
    
    return agent

def renderMetaballs2(balls, state):
    '''render slow metaball image'''
    from colorGradients import Gradientr
    
    h=300
    
    s = millis()
    img = createImage(width,h, ALPHA)
    
    
    for x in xrange(width):
        for y in xrange(h):
            
            ds = 0.0
            
            for ball in balls:
                ds += pow(ball.radius / dist(x,y, ball.position.x, ball.position.y),2)  #primitive additional calculation
            
            #print ds
            col = color(255*ds)
            #img = createImage(width,h, ALPHA)        
                
            # (lerpColor(color(0,0,0),color(255,255,255),col ))
            img.pixels[x+y*width] = col
    
    e = millis()
    print e-s
    
    
    img.updatePixels()
    image(img, 0, 0)
    
def renderMetaballs50(balls, logics,state, toFill=False):
    '''render fast metaball image'''
    from colorGradients import Gradientr
    bounds = state['bounds']
    G = Gradientr()
    
    h = 300
    img = createImage(width,h, ALPHA)
    
    
    for x in xrange(width):
        for y in xrange(h):
            
            ds = 0.0
            for ball in balls:
                ds += sq(ball.radius / dist(x,y, ball.position.x, ball.position.y))  #primitive additional calculation
            
            col = color(255*ds)                
            img.pixels[x+y*width] = col
            
    image(img,0,0)
    
    
        
    drawIso(img, rangeGen(20,220,bounds), G, state, toFill)
    

def rangeGen(Min, Max, steps):
    s = (Max-Min)/steps
    return xrange(Min, Max, s)

    e = millis()
    print e-s
    
    #for ball in balls:
    #    ball.crossViz(state)
    
def renderMetaballs60(balls, logics,state, myMB, toFill=False):
    '''render fast metaball image'''
    from colorGradients import Gradientr
    bounds = state['bounds']
    G = Gradientr()
    
    h = 300
    myMB.mb3(300,1040, [[b.radius, b.position.x, b.position.y] for b in state['agents']], state['bounds'], state['color'], toFill) 
#     img = get(0,0, width,h)
#         
#     drawIso(img, rangeGen(20,220,bounds), G, state, toFill)



def drawIso(img, ts, G, state, toFill=False):
    global finder        
    bounds = state['bounds']
        
    isoArray = []
        
    for t in ts:
        finder.setThreshold(t)
        finder.find([red(x) for x in img.pixels] )
            
        for k in xrange(finder.getNumContours()):
            isoArray.append( [finder.getContourPoints(k)])
        
    # blacken pixels
    fill(0)
    rect(0,0,1040,300)
        
    for i, tp in enumerate(isoArray):
        if toFill:
            noStroke()
            col = G.gradientAgent(float(i)/bounds, state['color'])
            fill(red(col), green(col), blue(col),50)
        else:
            noFill()
            stroke(G.gradientAgent(float(i)/bounds, state['color']))
                
        for t in tp:
            beginShape()
            for p in t:
                if p.x<=3: 
                    p.x-=4
                elif p.x>=width-3: 
                    p.x +=4
                    
                if p.y<=3: 
                    p.y -=4
                elif p.y>=297: 
                    p.y +=4
                    
                vertex(p.x, p.y)
            endShape(CLOSE)
        
        

    print 'counturs:', finder.getNumContours()
    
