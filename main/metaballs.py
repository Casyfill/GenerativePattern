

def renderMetaballs1(balls, logics,state):
    '''render slow metaball image'''
    from colorGradients import Gradientr
    
    h = 300
    
    s = millis()
    img = createImage(width,h, ALPHA)
    
    numBalls = len(balls)
    
    G = Gradientr()
    
    for x in xrange(width):
        for y in xrange(h):
            
            ds = 0.0
            
            for ball in balls:
                r = 0.5*ball.radius*ball.density*state['aSize']
                d = sq(r/dist(x,y, ball.position.x, ball.position.y)) # distance to pixel
                ds+=d
                
                #col += ball.radius / d   #primitive additional calculation
            
            #print sum(ds)
            D = ds
            
            col = logics(D, state, G)
                    
                
            # (lerpColor(color(0,0,0),color(255,255,255),col ))
            img.pixels[x+y*width] = col
    
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
    
    bounds = 10
    
    colrScheme = state['color']
    #print 'cS',colrScheme
    
    for b in xrange(bounds):
        #p = remap(i,80.0,500.0,0.0,1.0)
        wd-= i*0.02
        
        
        j = remap(float(b),0,bounds,0.3,5.0)
        
        
        if j<D<j+wd:
            c = remap(float(b),0,bounds,0.0,1.0)
            if state['rColor']: 
                c = 1-c
            col=G.gradientAgent(c,colrScheme )
            
    #print 'col:',col
            
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
                    
                
            # (lerpColor(color(0,0,0),color(255,255,255),col ))
            img.pixels[x+y*width] = col
    
    e = millis()
    print e-s
    
    
    img.updatePixels()
    image(img, 0, 0)
    
def renderMetaballs3(balls, state):
    '''render slow metaball image'''
    from colorGradients import Gradientr
    
    h=300
    
    
    s = millis()
    img = createImage(width,h, ALPHA)
    G = Gradientr()
    
    for x in xrange(width):
        for y in xrange(h):
            
            ds = 0.0
            if len(balls)<8: 
                power=2
            elif len(balls)<15:
                power = 4
            else: power = 6
            
            for ball in balls:
                ds += pow(ball.radius / dist(x,y, ball.position.x, ball.position.y),power)  #primitive additional calculation
            
            #print ds
            #if ds >1: ds=1
            
            col = G.gradientAgent(ds,state['color'])
            
                
            # (lerpColor(color(0,0,0),color(255,255,255),col ))
            img.pixels[x+y*width] = col
    
    
    
    
    img.updatePixels()
    image(img, 0, 0)
    e = millis()
    print e-s
    

