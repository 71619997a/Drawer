basefont = 0 

def setup():
    global basefont
    basefont = loadFont('Monospace821BT-Roman-24.vlw')

def between(a, b, c):  # if b between a and c
    return min(a, c) <= b <= max(a, c)