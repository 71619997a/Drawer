from Drawable import Drawable

class TextBox(Drawable):
    def __init__(self, x, y, s, col=0):
        self.x = x
        self.y = y
        self.s = s
        self.col = col
    
    def draw(self):
        stroke(self.col)
        text(self.x, self.y, self.s)
        