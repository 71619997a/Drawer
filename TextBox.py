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
        # if self.ft != 0: 
        #     textFont(self.ft, 24) 
        fill(self.col)
        text(self.s, self.x, self.y)
        print self.s, self.x, self.y
        