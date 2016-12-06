from Rectangle import Rectangle
from TextBox import TextBox
entities = []
IDLE = -1
RECTANG = 0
TEXT = 1
mode = TEXT
insmode = RECTANG
basefont = 0
def setup():
    global basefont
    size(200, 200)
    background(255)
    basefont = loadFont('Cambria-24.vlw')

def draw():
    background(255)
    fill(255, 255, 255, 0)
    if mode == RECTANG:
        entities[-1].update(mouseX, mouseY)
    for ent in entities:
        ent.draw()
    print entities
    
def mousePressed():
    global mode
    if mode == RECTANG:  # ending rectangle
        mode = IDLE
    elif mode == TEXT:  # new text box
        entities.append(TextBox(mouseX, mouseY, ''))
    else: # mode == IDLE
        mode = insmode
        if mode == RECTANG:  # beginning rectangle
            entities.append(Rectangle(mouseX, mouseY, mouseX, mouseY))
            
        
def keyPressed():
    global mode
    if mode == TEXT:
        entities[-1].update(key)


    