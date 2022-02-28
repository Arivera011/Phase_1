
x_dim = 500
y_dim = 500
color_mode = RGB 
color_max_value = x_dim

def set_color_mode():
    colorMode(color_mode, color_max_value)
    #colorMode(RGB, 255)

def update_agent_location(x_norm,y_norm):
    global agent_x, agent_y
    agent_x = x_norm * x_dim
    agent_y = y_norm * y_dim

def get_agent_location_xy():
    
    return agent_x, agent_y
    
def get_agent_location_color():
    
    r = agent_x * (color_max_value / x_dim)
    g = agent_y * (color_max_value / x_dim)
    b = 0
    
    return color(r, g, b)

def get_white():
    
    return color(color_max_value)
