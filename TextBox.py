from Drawable import Drawable
import utils

    
class TextBox(Drawable):
    def __init__(self, x, y, s, ft=0, ftsize=24, col=0):
        if ft == 0:
            ft = utils.basefont
        self.x = x
        self.y = y
        self.s = s
        self.col = col
        self.ft = ft
    
    def update(self, s):
        self.s += s
    
    def draw(self):
        print self.ft
        textFont(self.ft, 24) 
        fill(self.col)
        text(self.s, self.x, self.y)
        print self.s, self.x, self.y
        
    def collides(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2 <= 400  # whatever