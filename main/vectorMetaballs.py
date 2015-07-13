import mSquares as mS
import mb_misc as misc
import colorGradients as cG


def drawMetaballs(state, tofill=False, ):
    bounds = state['bounds']
    g = cG.Gradientr()
    
    if len(state['metaballs'])!=0 and tofill :    
        for j, cnts in enumerate(state['metaballs']):
            jx = float(j)/bounds # relative raratio
            aes = {'strokeWeight': 0.5 + (1-jx)*3, 'color':g.gradientAgent(jx, state['color']) }
            for c in cnts:
                if tofill:
                    misc.drawFills(c, aes)
                else:
                    misc.drawCurves(c, aes)
    else:
        cell_size = 16
    
        # generate Balls
        balls = []
        #filter agents
        agents = [a for a in state['agents'] if all([a.position.x>-200,a.position.x < width+200, a.position.y> -200, a.position.y < height+200 ])]
        print 'agents:', len(agents)
        for agent in agents:
            rads = [max(agent.radius,cell_size) + sq(3*i) for i in xrange(bounds)]
            balls.append(misc.ball(agent.position, PVector(0,0), rads))
        
    
        # generate GRID
        Squares = mS.SquareGrid(PVector(-100,-370,0), width+500, width+500,cell_size, bounds)
        lines = mS.defineLines(balls, Squares, bounds)
    
        
        for j in xrange(bounds-1,-1,-1): 
            jx = float(j)/bounds # relative raratio
        
            aes = {'strokeWeight':1, 'color':g.gradientAgent(jx, state['color']) }
            if len(lines[j])>2:
                cs = misc.cntrNew(lines[j], 3)
                for c in cs:
                    c = misc.smoothCurve(c, 0.6)
                    if tofill:
                        x = color(red(aes['color']), green(aes['color']), blue(aes['color']), 200)
                        aes['color'] = x
                        misc.drawFills(c, aes)
                    else:
                        
                        misc.drawCurves2(c, aes)
                state['metaballs'].append(cs)
        

    
