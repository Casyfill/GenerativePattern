from colorGradients import Gradientr

class Agent():
    
    position= PVector(0,0,0)
    dencity= 1
    radius = 1
    
    def __init__(self, position, density, radius):
        self.position = position
        self.density = density
        self.radius = radius
    
    def viz(self,state):
    
        position = self.position
        density = self.density
        radius = self.radius
        
        noStroke()
        #colorMode(HSB)
        #fill(map(position.z, -200, 200, 10, 30 )/(density/1.2), 255, 255, map(position.z, -200, 200, 255, 255))
        #mx = 30/(state['minM'][0]/1.2)
        #mn = 10/( state['maxM'][1]/1.2)
        #print mn,
        i = map(map(position.z, -200, 200, 10, 30 )/(density/1.2),0,state['cSharp'],0,1) # map parameters onto gradientRamp        
        if state['rColor']:
            i = 1-i
        
        fill(Gradientr(i, state['color']-1))
        
        r = radius*density*state['aSize']
        
        ellipseMode(CENTER)
        ellipse(position.x, position.y, r, r)
        
              
              
              
