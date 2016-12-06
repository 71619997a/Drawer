from Drawable import Drawable

basefont = 0
class TextBox(Drawable):
    print 'asd'
    def __init__(self, x, y, s, ft=0, ftsize=24, col=0):
        if basefont == 0:
            global basefont
            basefont = loadFont('Cambria-24.vlw')
        self.x = x
        self.y = y
        self.s = s
        self.col = col
        if ft == 0:
            self.ft = basefont
        else:
            self.ft = ft
    
    def update(self, s):
        self.s += s
    
    def draw(self):
        textFont(self.ft, 24) 
        fill(self.col)
        text(self.s, self.x, self.y)
        print self.s, self.x, self.y
        