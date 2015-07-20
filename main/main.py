## generative Pattern for webinars.ru
## by Philipp Kats, june 2015
##


add_library('controlP5')

import gui # all but main gui functions
import geomLogics as gL # alladvanced geometrical functions
import DistrPoints as dp
import metaballs as mb

from colorGradients import Gradientr
from com.metaballs import Metaballs

agents = []

controls = ()  # gui controls
state = {"cpointT":1.0, 
             "cRadius":150,
             "cDistr":50,
             'color':random(1.0,9.0),
             "shape":1,
             "mDist":100,
             "minM":[0.3,0.8],
             "maxM":[1.0,1.6],
             'aSize':1.0,
             'uid': int(random(1,10000)),
             'n': 10,
             'rColor': False,
             'cnt':1,
             'cSharp':38,
             'colorState':0,
             'cP' : PVector(0,0,0),
             'agents':[],
             'bounds':3,
             'metaballs':[]
             } # default states

colorState = 0
w , h = 1040, 420

def setup():
    global controls
    global state
    smooth()
    
    size(w,h)
    rect(0,300,w,150)
    
    background(0) #toolbar color

    #ControlPanel     
    fill(100)
    noStroke()
    
    noStroke()
    
    
    controls = controlPanel(state) # main GUI function
    
    
  

def draw():
    # update state. if it changed, redraw canvas

    oldState = gui.updateState(colorState, state,controls)
    
    if oldState==state:
        return
    
    print 'state updated!'
    
    
    #black canvas
    fill(0)
    noStroke()
    rect(0,0,w,300)     
    
    if state['colorState']!=0:
        g = Gradientr()
        g.gradiantBack(state['color'], state['cP'],w, state['rColor'])
    
    
    randomSeed(state['uid'])
    print 'uid:', state['uid']
    
    
    dp.popPlane(state)
    
    
    
    #ControlPanel     
    fill(100)
    noStroke()
    
    rect(0,300,w,h-300)
    

def controlPanel(state):
    global cp5
    cp5 = ControlP5(this)
    
    #GENERAL
    
    # slider 1, central point position
    sl1 = cp5.addSlider("central Point").setPosition(15, 315).setRange(0.00,1.00).setValue(state['cpointT'])
    gui.customizeSlider(sl1)
    
    # slider 2, circle radius
    sl2 = cp5.addSlider("circle radius").setPosition(15, 335).setRange(0,500).setValue(state['cRadius'])
    gui.customizeSlider(sl2)
    
    # slider 3, circle distortion
    sl3 = cp5.addSlider("circle distortion").setPosition(15, 355).setRange(0,100).setValue(state['cDistr'])
    gui.customizeSlider(sl3)
    
    #numBALLS - balls (num)
    numB = cp5.addTextfield("Balls").setPosition(15,375).setSize(60,15).setAutoClear(False)
    numB.setText(str(state['n']))
    gui.styleGUI(numB)
    
    #numberBox - uID (seed)
    bounds = cp5.addTextfield("bounds").setPosition(90,375).setSize(30,15).setAutoClear(False)
    bounds.setText(str(state['bounds']))
    #uID.addListener(TextListener())
    gui.styleGUI(bounds)
    
    ## STATES
    
    # slider 4, colorMode TODO: redesign to integers
    sl4 = cp5.addSlider("color Mode").setPosition(300, 315).setRange(1,10).setValue(state['color'])
    gui.customizeSlider(sl4)
    
    sl8 = cp5.addSlider("color sharpness").setPosition(300, 335).setRange(20,45).setValue(state['cSharp'])
    gui.customizeSlider(sl8)
    
    # slider 5, shapeMode  TODO: redesign to integers
    sl5 = cp5.addSlider("shape Mode").setPosition(300, 355).setRange(1,3).setValue(state['shape'])
    gui.customizeSlider(sl5)
    
    
    # toggle reverse color
    tgl1 = cp5.addToggle("reverse color").setPosition(300, 375).setValue(state['rColor'])
    tgl1.setSize(30,15)
    
    b2 = cp5.addBang("CS").setPosition(370, 375).setSize(60, 20).setLabel("CS")
    b2.addListener(bangListener2())
    gui.customizeBang(b2)
    b2.setSize(15, 15)
    
    
    
    ## MODIFIER PARAMS
    
    # slider 6 - distance toward modified objects
    sl6  = cp5.addSlider("mod distance").setPosition(600, 315).setRange(0,500).setValue(state['mDist'])
    gui.customizeSlider(sl6)
    gui.styleGUI(tgl1)
    
    # rangeMin - scale of change for min deformation
    rng1 = cp5.addRange("min Multiplier").setBroadcast(False)


    rng1.setPosition(600,335)
    rng1.setSize(200,15)
    rng1.setHandleSize(12)
    rng1.setRange(0.1,1)
    rng1.setRangeValues(state['minM'][0], state['minM'][1])
    rng1.addListener( 
        lambda e: saveState(e,'minM'))            
    rng1.setBroadcast(True)
    
    gui.styleGUI(rng1)
    
    # rangeMax - scale of change for max deformation
    rng2 = cp5.addRange("max Multiplier").setBroadcast(False)

     
    rng2.setPosition(600,355)
    rng2.setSize(200,15)
    rng2.setHandleSize(12)
    rng2.setRange(1.0,2.0)
    rng2.setRangeValues(state['maxM'][0], state['maxM'][1])
    rng2.addListener(
        lambda e: saveState(e,'maxM'))       
    rng2.setBroadcast(True)
    
    gui.styleGUI(rng2)  
    
    sl7 = cp5.addSlider("agent Size").setPosition(600, 375).setRange(0.1,3.0).setValue(state['aSize'])
    gui.customizeSlider(sl7)
    
    # metaballs bang 1
    b3 = cp5.addBang("metaballs1").setPosition(424, 375).setSize(60, 20).setLabel("MB1")
    b3.addListener(bangListener3())
    gui.customizeBang(b3)
    b3.setSize(15, 15)
    
    # metaballs bang 2
    b31 = cp5.addBang("metaballs12").setPosition(444, 375).setSize(60, 20).setLabel("MB2")
    b31.addListener(bangListener31())
    gui.customizeBang(b31)
    b31.setSize(15, 15)
    
    # metaballs bang 3
    b4 = cp5.addBang("metaballs2").setPosition(464, 375).setSize(60, 20).setLabel("MB3")
    b4.addListener(bangListener4())
    gui.customizeBang(b4)
    b4.setSize(15, 15)
    
    # metaballs bang 4
    b5 = cp5.addBang("metaballs3").setPosition(484, 375).setSize(60, 20).setLabel("MB4")
    b5.addListener(bangListener5())
    gui.customizeBang(b5)
    b5.setSize(15, 15)
    

    ## GENERAL OUT
    
    #numberBox - uID (seed)
    uID = cp5.addTextfield("uID").setPosition(w-75,315).setSize(60,15).setAutoClear(False)
    uID.setText(str(state['uid']))
    #uID.addListener(TextListener())
    gui.styleGUI(uID)
    
    # save img button
    b = cp5.addBang("bang").setPosition(w-75, 350).setSize(60, 20).setLabel("Save image")
    b.addListener(bangListener1())
    gui.customizeBang(b)
    return (sl1,sl2,sl3,sl4,sl5,sl6,sl7, rng1,rng2, uID, tgl1, sl8, numB,bounds)


class TextListener(ControlListener):
    def controlEvent(self, e):
        try: 
            state['uid'] = int(e.getStringValue())
        except:
            
            pass
        print state['uid']
         

def saveState(v, tag):
    global state
    
    state[tag]=v
    
class bangListener1(ControlListener):
    def controlEvent(self, e):
        global state
        img  = get(0, 0, 1040, 300)
        path = "img/pattern###.jpg".replace('###',str(state['uid'])+'_'+str(state['cnt']))
        img.save(path)
        print (path + 'file saved in the same folder as applet!')
        state['cnt']+=1 

class bangListener2(ControlListener):
    def controlEvent(self, e):
        global colorState
        
        x = colorState
        if x ==2:
            x=0
        else: x+=1 
       
        colorState = x
        print 'colorState is:', colorState

class bangListener3(ControlListener):
    def controlEvent(self, e):
        global state
        
        #dAgents= mb.delocate(state['agents'],state) 
        rect(0,0,1040,300)
        print 'start drawing'
        mb.renderMetaballs1(state['agents'], mb.draw1, state)
        
        #ControlPanel     
        fill(100)
        noStroke()
    
        rect(0,300,w,h-300)
        print 'done drawing'
            

class bangListener4(ControlListener):
    def controlEvent(self, e):
        s = millis()
        global state
        print 'start drawing Isocurves'
        fill(0)
        rect(0,0,1040,300)
        
        mb.renderMetaballs50(state['agents'], mb.draw1, state, toFill=False)
        
        #ControlPanel     
        fill(100)
        noStroke()
    
        rect(0,300,w,h-300)
        e = millis()
        print 'metaball took %d seconds' % ((e-s)/1000)
        print 'done drawing'


class bangListener5(ControlListener):
    def controlEvent(self, e):
        s = millis()
        global state
        print 'start drawing isolines'
        fill(0)
        rect(0,0,1040,300)
        
        #vMb.drawMetaballs(state, tofill=True)
        mb.renderMetaballs50(state['agents'], mb.draw1, state, toFill=True)
         
        #ControlPanel     
        fill(100)
        noStroke()
    
        rect(0,300,w,h-300)
        e = millis()
        print 'metaball took %d seconds' %((e-s)/1000)
        print 'done drawing'
        

class bangListener31(ControlListener):
    def controlEvent(self, e):
        global state
        
        #dAgents= mb.delocate(state['agents'],state) 
        rect(0,0,1040,300)
        print 'start drawing'
        mb.renderMetaballs1(state['agents'], mb.draw2, state)
        
        #ControlPanel     
        fill(100)
        noStroke()
    
        rect(0,300,w,h-300)
        print 'done drawing'
        
        
    
    
