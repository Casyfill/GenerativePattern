
    
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

