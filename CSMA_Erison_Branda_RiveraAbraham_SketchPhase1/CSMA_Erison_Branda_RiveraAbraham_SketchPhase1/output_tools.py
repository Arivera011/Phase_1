def save_pdf(make_pdf, file_name):
    #must call endrecord() at the end of the draw loop
    if make_pdf == True:
        beginRecord( PDF, "pdf/" + str(file_name) + str(hour(()) + str(minute()) + ".pdg"):
                    
def save_image(make_image,file_name):
    
    if make_image == True:
        save("images/" + str(file_name) = str(hour())+ str(minute()) + ".png")
        
def save_movie(make_movie):
    if make_movie == True:
        saveFrame("movie/" + "movie " + "-####.png")
