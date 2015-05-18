

def unpack_rgb(rgb):
    r = (0xff0000 & rgb) >> 16
    g = (0x00ff00 & rgb) >> 8
    b = (0x0000ff & rgb)
    return r,g,b

def pack_rgb(r,g,b):
    return (min(r,0xff) << 16) + (min(g,0xff) << 8) + min(b,0xff)    

def calc_brightness((r,g,b), brightness):
    r = int(r*brightness)
    g = int(g*brightness)
    b = int(b*brightness)
    return (min(r,255),min(255,g),min(255,b))

def calc_flash((r,g,b), addition):
    r += addition
    g += addition
    b += addition
    return (min(r,255),min(255,g),min(255,b))

def calc_gray((r,g,b), hue):
    middle = (r+g+b) / 3.0
    ghue = 1-hue
    r = int(hue*r + ghue*middle)
    g = int(hue*g + ghue*middle)
    b = int(hue*b + ghue*middle)
    return (r,g,b)    

