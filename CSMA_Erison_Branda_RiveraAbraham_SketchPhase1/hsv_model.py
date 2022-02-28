
x_dim = 500
y_dim = 500
color_mode = HSB 
radius_max = x_dim/3
v_val = 100

def set_color_mode():
    colorMode(color_mode,360, radius_max, v_val)


def get_color_values():
    
    proc_color= get_agent_location_color()
    
    h = round(hue(proc_color),2)
    s = round(saturation(proc_color),2)
    v = round(brightness(proc_color),2)
    
    return h,s,v

def get_white():
    
    return color(0,0,v_val)

def get_agent_location():
    return agent_x, agent_y


#def update_agent_location(angle_norm,radius_norm):
    #global angle_deg, radius

    
    #angle_deg  = angle_norm*360
    #radius     = radius_norm* radius_max
    
#def get_agent_location_xy():
    
    #agent_x = cos(radians(angle_deg))* radius + x_dim/2
    #agent_y = sin(radians(angle_deg))* radius + y_dim/2

    #return agent_x, agent_y
    
#def get_agent_location_color():
    
    #angle = radians(current_h_val)
    
    #h = angle_deg
    #s = radius 
    #v = v_val
    
    #itll give it a number for this computation  
