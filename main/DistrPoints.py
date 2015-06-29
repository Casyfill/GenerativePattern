# 
#

def popPlane(p, state):
    
    pushMatrix()
    translate(p.x, p.y)
    rotate(-p.z)
    
    inPlane(p,state)
    popMatrix()

def inPlane(p, state):
    
    
    rectMode(CENTER)
    noFill()
    stroke(255)
    strokeWeight(2)
    rect(0, 0,state['cRadius'],state['cRadius'])
    rectMode(CORNER)

    
