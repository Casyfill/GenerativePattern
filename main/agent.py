
class Agent():
    
    position= PVector(0,0,0)
    dencity= 1
    radius = 1
    
    def __init__(self, position, density, radius):
        self.position = position
        self.density = density
        self.radius = radius
    
    def viz(self):
        position = self.position
        density = self.density
        radius = self.radius
        
        colorMode(HSB)
        noStroke()
        fill(map(position.z, -200, 200, 10, 30 )/(density/1.2), 255, 255, map(position.z, -200, 200, 255, 255))
        ellipseMode(CENTER)
        ellipse(position.x, position.y, radius*density, radius*density)
        
              
              
              
