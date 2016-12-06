from Rectangle import Rectangle
from TextBox import TextBox
from setup import setup as setupall

entities = []
IDLE = -1
RECTANG = 0
TEXT = 1
ERASING = 2
mode = TEXT
insmode = RECTANG

def setup():
    size(200, 200)
    background(255)
    setupall()

def draw():
    background(255)
    fill(255, 255, 255, 0)
    if mode == RECTANG:
        updent(mouseX, mouseY)
    for ent in entities:
        ent.draw()
    print entities
    
def mousePressed():
    global mode
    if mode == RECTANG:  # ending rectangle
        mode = IDLE
    elif mode == TEXT:  # new text box
        entities.append(TextBox(mouseX, mouseY, ''))
    elif mode == ERASING:
        for i in range(len(entities) - 2, -1, -1):  # start from latest entity, not including eraser itself
            if entities[i].collides(mouseX, mouseY):
                del entities[i]
                break
    else: # mode == IDLE
        mode = insmode
        if mode == RECTANG:  # beginning rectangle
            entities.append(Rectangle(mouseX, mouseY, mouseX, mouseY))
            
        
def keyPressed():
    global mode
    if mode == TEXT:
        updent(key)

def updent(*args, **kwargs):
    if len(entities):
        entities[-1].update(*args, **kwargs)

    