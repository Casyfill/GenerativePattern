## generative Pattern for webinars.ru
## by Philipp Kats, june 2015
##


add_library('controlP5')

w , h = 1040, 450
def setup():
    background(100) #toolbar color
    size(w,h)
    
    controlPanel()
    
    

def draw():

    fill(0)
    noStroke()
    rect(0,0,w,300)
    #ell    
    
    #cpointT =  cp5.get(Slider,"central Point").getValue()
    
    ellipse(w/2,h/2,30,30)


def controlPanel():
    global cp5
    cp5 = ControlP5(this)
    
    #GENERAL
    
    # slider 1, central point position
    sl1 = cp5.addSlider("central Point").setPosition(15, 315).setRange(0,100).setValue(100)
    customizeSlider(sl1)
    
    # slider 2, circle radius
    sl2 = cp5.addSlider("circle radius").setPosition(15, 335).setRange(0,100).setValue(50)
    customizeSlider(sl2)
    
    # slider 3, circle distortion
    sl3 = cp5.addSlider("circle distortion").setPosition(15, 355).setRange(0,100).setValue(50)
    customizeSlider(sl3)
    
    ## STATES
    
    # slider 4, colorMode TODO: redesign to integers
    sl4 = cp5.addSlider("color Mode").setPosition(300, 315).setRange(1,6).setValue(1)
    customizeSlider(sl4)
    
    # slider 5, shapeMode  TODO: redesign to integers
    sl5 = cp5.addSlider("shape Mode").setPosition(300, 335).setRange(1,3).setValue(1)
    customizeSlider(sl5)
    
    
    ## MODIFIER PARAMS
    
    # slider 6 - distance toward modified objects
    sl6  = cp5.addSlider("mod distance").setPosition(600, 315).setRange(0,500).setValue(300)
    customizeSlider(sl6)
    
    # rangeMin - scale of change for min deformation
    rng1 = cp5.addRange("min Multiplier")

    rng1.setBroadcast(False) 
    rng1.setPosition(600,335)
    rng1.setSize(200,15)
    rng1.setHandleSize(12)
    rng1.setRange(0.1,1)
    rng1.setRangeValues(0.3,0.8)        
    rng1.setBroadcast(True)
    
    styleGUI(rng1)
    
    # rangeMax - scale of change for max deformation
    rng2 = cp5.addRange("max Multiplier")

    rng2.setBroadcast(False) 
    rng2.setPosition(600,355)
    rng2.setSize(200,15)
    rng2.setHandleSize(12)
    rng2.setRange(1.0,2.0)
    rng2.setRangeValues(1.0,1.6)        
    rng2.setBroadcast(True)
    
    styleGUI(rng2)  
    
    
    ## GENERAL OUT
    
    #numberBox - uID (seed)
    uID = cp5.addTextfield("seed").setPosition(w-75,315).setSize(60,15).setAutoClear(False)
    uID.setDefaultValue(9999)
    styleGUI(uID)
    # save img button
    b = cp5.addBang("bang").setPosition(w-75, 350).setSize(60, 20).setLabel("Save image")
    customizeBang(b)
    
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
  
  
def bang():
    #supposed to react to the bang button
    print('saved!')

