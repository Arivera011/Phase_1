add_library('sound')

import hsv_model as model 
import microphone
import output_tools as output 
import os

from recorder import Recorder 

stop_point = 500 #frame rate of the sketch will stop onces hitting the given frame 

file_name = os.path.basename(__file__)

Recorder()

def setup():
    global agent_record,stop_point, file_name, calibri_font
    size(model.x_dim,model.y_dim)
    model.set_color_mode()#change to set color mode in module 
    microphone.initialize(this, AudioIn, Amplitude)
    microphone.sensitivity = 3.0
    frameRate(20)
    
    pixelDensity(2)
    
    agent_record= Recorder() # start to create pdf files for a process of all the work output 
    
    calibri_font = createFont("calibri",15) #the font was imported to the file folders to be define and has two arguments (font,size)
    output.save_pdf(False,file_name)
    
    
def draw():
    sound_level = microphone.get_level()

    
    agent_param_0 = sound_level
    agent_param_1 = 0.5
    
    #model.current_h_val = 360*sound_level
    
    model.update_agent_location(agent_param_0,agent_param_1)
    #color_1, color_2, color_3 = model.get_current_color_values()
    
    render()
    
    #render(color_1, color_2, color_3)
    
    if frameCount == stop_point:
        noLoop()
        endRecord()

def render():
    #background(model.get_agent_location_color())
    #odject changing the crosshair 
    #stroke(model.get_white())
    
    
    noStroke()
    background(model.get_white())
    
    color_val= model.get_agent_location_color()
    color_vals = agent_record.get_recorded_color(color_val)
    
    x,y = model.get_agent_location_xy()
    agent_locations = agent_record.get_recorded_location(x,y)
    
    #too make a list  loop
    #loop is for the background and the i is whatever list number you give it minus 1
    for i in range(len(color_vals)):
        
        background(color_vals[i-1])
        
        
    
    #every item will be colored example of a list of 100 
    for i in range (len(color_vals)):
        fill(color_vals[i])
        x0,y0 = agent_locations[i]
        rect(x0,y0, 20,20)
        
    textFont(calibri_font) #define the font given in global
    label = model.get_color_values()
    fill(model.get_white()) #give the font a color 
    text(str(label), x, y)
    
        

    

    #print(Recorder())
 
