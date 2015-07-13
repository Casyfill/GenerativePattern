from colorGradients import Gradientr

class Agent():
    
    position= PVector(0,0,0)
    dencity= 1
    radius = 1
    rRadius = 1
    def __init__(self, position, density, radius, multiplicator):
        self.position = position
        self.density = density
        self.radius = radius
        self.rRadius = radius*density* multiplicator
    
    def viz(self,state):
    
        position = self.position
        density = self.density
        radius = self.radius
        
        noStroke()
        
        i = map(map(position.z, -200, 200, 10, 30 )/(density/1.2),0,state['cSharp'],0,1) # map parameters onto gradientRamp        
        if state['rColor']:
            i = 1-i
        
        if state['colorState']==0:
            G = Gradientr()
            fill(G.gradientAgent(i, state['color']))
        elif state['colorState']==1:
            fill(0)
        elif state['colorState']==2:
            fill(255)
        
        self.rRadius = radius*density*state['aSize']
        
        
        ellipseMode(CENTER)
        ellipse(position.x, position.y, self.rRadius, self.rRadius)
    
    def crossViz(self,state):
        stroke(255)
        noFill()
        r = self.radius*self.density*state['aSize']
        
        line(self.position.x -r/2,self.position.y,self.position.x + r/2,self.position.y)
        line(self.position.x,self.position.y-r/2,self.position.x ,self.position.y+r/2)
        ellipseMode(CENTER)
        ellipse(self.position.x, self.position.y, r, r)
        
        
              
              
              
