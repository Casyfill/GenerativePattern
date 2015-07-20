import geomLogics as gL
    
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

def updateState(cs, state,controls):
    oldState = state.copy()
    state['cpointT'] = controls[0].getValue()
    state['cRadius'] = controls[1].getValue()
    state['cDistr'] = controls[2].getValue()
    state['color'] = controls[3].getValue()-1
    state['shape'] = controls[4].getValue()
    state['mDist'] = controls[5].getValue()
    state['aSize'] = controls[6].getValue()
    state['minM'] = controls[7].arrayValue()
    state['maxM'] = controls[8].arrayValue()
    state['rColor'] = controls[10].getValue() #toggle
    state['cSharp'] = controls[11].getValue()
    state['colorState'] = cs
    state['cP'] = gL.defineCenter(state['cpointT'])
    try:
        state['uid'] = int(controls[9].getStringValue())
    except:
        #println("caution: uID should be numeric!")
        pass
    
    try:
        state['n'] = int(controls[12].getStringValue())
    except:
        #println("caution: numB should be numeric!")
        pass
        
    try:
        state['bounds'] = int(controls[13].getStringValue())
    except:
        #println("caution: uID should be numeric!")
        pass

    
    return oldState
  
def bang():
    #supposed to react to the bang button
    print('saved!')


