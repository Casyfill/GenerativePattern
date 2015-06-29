## generative Pattern for webinars.ru
## by Philipp Kats, june 2015
##


add_library('controlP5')

controls = ()
state = {}
i = 1  
w , h = 1040, 420

def setup():
    global controls
    global state
    state = {"cpointT":100, 
             "cRadius":50,
             "cDistr":50,
             'color':1,
             "shape":1,
             "mDist":300,
             "minM":[0.3,0.8],
             "maxM":[1,1.6],
             'uID':9999
             } # stateParams
    
    background(100) #toolbar color
    size(w,h)
    
    controls =controlPanel(state) # main GUI function
    
    
  

def draw():
    reDraw = False
    #update state! 
    global i    
    oldState = updateState(state,controls)
    
    if oldState==state:
        return
    
    print 'lalala', i
    i+=1
    
    fill(0)
    noStroke()
    rect(0,0,w,300)
    
    
    textSize(16)
    fill(255)
    text(state['cpointT'], 10, 30)   
    
    
    
    #ellipse(w/2,h/2,30,30)


def controlPanel(state):
    global cp5
    cp5 = ControlP5(this)
    
    #GENERAL
    
    # slider 1, central point position
    sl1 = cp5.addSlider("central Point").setPosition(15, 315).setRange(0,100).setValue(state['cpointT'])
    customizeSlider(sl1)
    
    # slider 2, circle radius
    sl2 = cp5.addSlider("circle radius").setPosition(15, 335).setRange(0,100).setValue(state['cRadius'])
    customizeSlider(sl2)
    
    # slider 3, circle distortion
    sl3 = cp5.addSlider("circle distortion").setPosition(15, 355).setRange(0,100).setValue(state['cDistr'])
    customizeSlider(sl3)
    
    ## STATES
    
    # slider 4, colorMode TODO: redesign to integers
    sl4 = cp5.addSlider("color Mode").setPosition(300, 315).setRange(1,6).setValue(state['color'])
    customizeSlider(sl4)
    
    # slider 5, shapeMode  TODO: redesign to integers
    sl5 = cp5.addSlider("shape Mode").setPosition(300, 335).setRange(1,3).setValue(state['shape'])
    customizeSlider(sl5)
    
    
    ## MODIFIER PARAMS
    
    # slider 6 - distance toward modified objects
    sl6  = cp5.addSlider("mod distance").setPosition(600, 315).setRange(0,500).setValue(state['mDist'])
    customizeSlider(sl6)
    
    # rangeMin - scale of change for min deformation
    rng1 = cp5.addRange("min Multiplier")

    rng1.setBroadcast(False) 
    rng1.setPosition(600,335)
    rng1.setSize(200,15)
    rng1.setHandleSize(12)
    rng1.setRange(0.1,1)
    rng1.setRangeValues(state['minM'][0], state['minM'][1])        
    rng1.setBroadcast(True)
    
    styleGUI(rng1)
    
    # rangeMax - scale of change for max deformation
    rng2 = cp5.addRange("max Multiplier")

    rng2.setBroadcast(False) 
    rng2.setPosition(600,355)
    rng2.setSize(200,15)
    rng2.setHandleSize(12)
    rng2.setRange(1.0,2.0)
    rng2.setRangeValues(state['maxM'][0], state['maxM'][1])        
    rng2.setBroadcast(True)
    
    styleGUI(rng2)  
    
    
    ## GENERAL OUT
    
    #numberBox - uID (seed)
    uID = cp5.addTextfield("seed").setPosition(w-75,315).setSize(60,15).setAutoClear(False)
    uID.setText(str(state['uID']))
    styleGUI(uID)
    # save img button
    b = cp5.addBang("bang").setPosition(w-75, 350).setSize(60, 20).setLabel("Save image")
    customizeBang(b)
    return (sl1,sl2,sl3,sl4,sl5,sl6, rng1,rng2, uID)
    
def styleGUI(o):
    o.setColorForeground(color(125))
    o.setColorActive(color(150))
    o.setColorValue(color(255))
    o.setColorBackground(color(70))
            
def customizeBang(b):
    styleGUI(b)
    


def customizeSlider(slider):
  # a convenience function to customize a DropdownList
  slider.setSize(200, 15)
  styleGUI(slider)

def updateState(state,controls):
    oldState = state.copy()
    state['cpointT'] = controls[0].getValue()
    state['cRadius'] = controls[1].getValue()
    state['cDistr'] = controls[2].getValue()
    state['color'] = controls[3].getValue()
    state['shape'] = controls[4].getValue()
    state['mDIst'] = controls[5].getValue()
    state['minM'] = controls[6].getValue()
    state['maxM'] = controls[7].getValue()
    try:
        state['uID'] = int(controls[8].getValue())
    except:
        state['uID'] = 9999
        println("caution: uID should be numeric!")
    return oldState
  
def bang():
    #supposed to react to the bang button
    print('saved!')

