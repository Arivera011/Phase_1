class Recorder:
    
    def __init__(self):
        
        
        self.location = []
        self.color_val= []
        
    def get_recorded_location (self,x,y):
        
        self.location.append((x,y))
        
        #set a max
        if len(self.location) > 500:
            
            #trim with pop
            self.location.pop(0)
        
            
            #see if there is erro hence the print    
            
        print(self.location)
        
        return(self.location)
    
    def get_recorded_color(self,color_value):
        
        self.color_val.append(color_value)
        
        if len(self.color_val) > 500:
            self.color_val.pop(0)
            
        return(self.color_val)
    
    
        
        
            
            
