from Rectangle import Rectangle
from TextBox import TextBox
entities = []
IDLE = -1
RECTANG = 0
TEXT = 1
mode = IDLE
insmode = RECTANG
def setup():
    size(200, 200)
    background(255)

def draw():
    background(255)
    fill(255, 255, 255, 0)
    if mode == RECTANG:
        entities[-1].update(mouseX, mouseY)
    for ent in entities:
        ent.draw()
    # print entities
    
def mouseClicked():
    global mode
    if mode == insmode: mode = IDLE
    elif mode == IDLE: 
        mode = insmode
        if mode == RECTANG:
            entities.append(Rectangle(mouseX, mouseY, mouseX, mouseY))
        elif mode == TEXT:
            entities.append(TextBox(mouseX, mouseY, ''))
        
def keyPressed():
    if mode == TEXT:
        entities[-1].update(key)


    
