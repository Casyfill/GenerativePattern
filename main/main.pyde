## generative Pattern for webinars.ru
## by Philipp Kats, june 2015
##

add_library('controlP5')
import gui # all but main gui functions
import geomLogics as gL # alladvanced geometrical functions
import DistrPoints as dp


controls = ()  # gui controls
state = {"cpointT":1.0, 
             "cRadius":300,
             "cDistr":50,
             'color':random(1,10),
             "shape":1,
             "mDist":250,
             "minM":[0.3,0.8],
             "maxM":[1.0,1.6],
             'aSize':1.0,
             'uid': int(random(1,10000)),
             'n': 400,
             'rColor': False,
             'cnt':1,
             'cSharp':38
             } # default states

w , h = 1040, 420

def setup():
    global controls
    global state
    smooth()
    
    background(0) #toolbar color
    size(w,h)
    
    #ControlPanel     
    fill(100)
    noStroke()
    
    noStroke()
    rect(0,300,w,150)
    
    controls = controlPanel(state) # main GUI function
    
    
  

def draw():
    # update state. if it changed, redraw canvas

    oldState = gui.updateState(state,controls)
    
    if oldState==state:
        return
    
    print 'state updated!'
    #black canvas     
    fill(0)
    noStroke()
    rect(0,0,w,300)
    randomSeed(state['uid'])
    print 'uid:', state['uid']
    
    c = gL.defineCenter(state['cpointT'])
    
    dp.popPlane(c,state)
    
    
    
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
    
    ## GENERAL OUT
    
    #numberBox - uID (seed)
    uID = cp5.addTextfield("uID").setPosition(w-75,315).setSize(60,15).setAutoClear(False)
    uID.setText(str(state['uid']))
    #uID.addListener(TextListener())
    gui.styleGUI(uID)
    
    # save img button
    b = cp5.addBang("bang").setPosition(w-75, 350).setSize(60, 20).setLabel("Save image")
    b.addListener(bangListener())
    gui.customizeBang(b)
    return (sl1,sl2,sl3,sl4,sl5,sl6,sl7, rng1,rng2, uID, tgl1, sl8)


class TextListener(ControlListener):
    def controlEvent(self, e):
        try: 
            state['uid'] = int(e.getStringValue())
        except:
            print "caution: uID should be numeric!"
            pass
        print state['uid']
         

def saveState(v, tag):
    global state
    
    state[tag]=v
    
class bangListener(ControlListener):
    def controlEvent(self, e):
        global state
        img  = get(0, 0, 1040, 300)
        path = "img/pattern###.jpg".replace('###',str(state['uid'])+'_'+str(state['cnt']))
        img.save(path)
        print (path + 'file saved in the same folder as applet!')
        state['cnt']+=1 


