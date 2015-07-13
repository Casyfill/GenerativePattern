#import java.util.Random as rnd
import geomLogics as gL
from agent import Agent
from metaballs import delocateOne

def popPlane(state):    
    inPlane(state)
    
def inPlane(state):
    
    agents = populateAgents(state)
    agents.sort(key=lambda x: x.position.z)
    vizAgents(agents,state)
    
    state['agents'] = agents

def populateAgents(state):
    
    shift = random(360)
    
    p = state['cP']
    t = state['cpointT']
    
    
    agents = []
    
    for x in xrange(state['n']):
        rad = map(round(randomGaussian()*15), 0, 35, 5, 100)
        zDepth = map(rad, 5, 150, -200, 200)
        ang = random(360)
        Dist = map(rad, 0, 150, state['cRadius'], 0) + random(-state['cDistr'], state['cDistr'])
        
            
        density = 1.0
        if Dist>state['mDist']:
            
            if ang>180:
                density *=random(state['minM'][0],state['minM'][1])
            else:
                density *=random(state['maxM'][0],state['maxM'][1])
        
        xy = gL.pointCyl(PVector(0,0), Dist, shift+ang)
        xy.z = zDepth
        
        a = delocateOne(Agent( xy, density, rad, state['aSize'] ), state['cP'], state['cpointT'])
        agents.append(a)
    return agents

def vizAgents(agents,state):
    for agent in agents:
        agent.viz(state)
    
    
