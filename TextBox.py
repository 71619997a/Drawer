from Drawable import Drawable

class TextBox(Drawable):
    def __init__(self, x, y, s, ft=0, col=0):
        self.x = x
        self.y = y
        self.s = s
        self.col = col
        self.ft = ft
    
    def update(self, s):
        self.s += s
    
    def draw(self):
        # textFont(self.ft) 
        stroke(self.col)
        text(self.x, self.y, self.s)
        
