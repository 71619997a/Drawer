from Drawable import Drawable

class Rectangle(Drawable):
    def __init__(self, x1, y1, x2, y2, border=0, filler=color(255, 255, 255, 0)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.border = border
        self.filler = filler
        
    def update(self, newX, newY):
        self.x2 = newX
        self.y2 = newY
    
    def draw(self):
        stroke(self.border)
        fill(self.filler)
        rect(self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)
        
        