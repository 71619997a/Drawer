from Rectangle import Rectangle

entities = []
IDLE = -1
RECTANG = 0
mode = IDLE
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
    if mode == RECTANG: mode = IDLE
    elif mode == IDLE: mode = RECTANG
    entities.append(Rectangle(mouseX, mouseY, mouseX, mouseY))


    