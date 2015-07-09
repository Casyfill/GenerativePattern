
class Gradientr(object):
    
    colorRamps = [
                  [color(169,169,169),color(45,45,45)],
                  [color(245,254,53),color(252,156,38)],
                  [color(252,151,41),color(251,15,33)],
                  [color(251,34,34),color(150,38,250)],
                  [color(233,34,252),color(36,59,251)],
                  [color(252,178,44),color(181,254,52)],
                  [color(43,254,47),color(253,227,50)],
                  [color(55,253,254),color(63,254,48)],
                  [color(36,113,252),color(43,254,130)],
                  [color(45,30,251),color(52,242,254)],
                  ]
    
    def gradientAgent(self, i, plt):
        # return a graient color within chosen palette 
        if i>1.0:
            i=1.0
        elif i<0.0:
            i=0.0
    
        p1 = floor(plt)
        p2 = ceil(plt)
        
        c1 =  lerpColor(self.colorRamps[p1][0],self.colorRamps[p1][1],i)
        c2 =  lerpColor(self.colorRamps[p2][0],self.colorRamps[p2][1],i)
    
        return lerpColor(c1,c2, plt-p1)
    
    def gradiantBack(self, plt, center,w, reverse):
        
    
        
        p1 = floor(plt)
        p2 = ceil(plt)
        
        mx = (w - center.x)*2 + 30
        #mx= 1700 # max width of sircle
        noStroke()
        for r in xrange(mx,0,-1):
            if reverse:
                i = map(r,0,mx,1,0)
            else:
                i = map(r,0,mx,0,1)
            
            fill(lerpColor(self.colorRamps[p1][0],self.colorRamps[p1][1],i));
            ellipse(center.x,center.y, r,r)
    
    
    
