# Circuit Python

import displayio
from adafruit_gizmo import tft_gizmo
from line_art import LineArt

# Get a drawing canvas on the gizmo
display = tft_gizmo.TFT_Gizmo()
splash = displayio.Group(max_size=10)
display.show(splash)
color_bitmap = displayio.Bitmap(240, 240, 32)
color_palette = displayio.Palette(32)
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Line function for the gizmo
def line(x0, y0, x1, y1,color):    
    # Line drawing function.  Will draw a single pixel wide line starting at
    # x0, y0 and ending at x1, y1.
    steep = abs(y1 - y0) > abs(x1 - x0)
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = abs(y1 - y0)
    err = dx // 2
    ystep = 0
    if y0 < y1:
        ystep = 1
    else:
        ystep = -1
    while x0 <= x1:
        if steep:
            color_bitmap[y0,x0] = color
            #self._pixel(y0, x0, *args, **kwargs)
        else:
            color_bitmap[x0,y0] = color
            #self._pixel(x0, y0, *args, **kwargs)
        err -= dy
        if err < 0:
            y0 += ystep
            err += dx
        x0 += 1

# A few section configurations for the gizmo hardware
CONFIGS = {
    # Four quadrants over the entire display
    'FOUR' : {
        'xofs' : 0,
        'yofs' : 0,
        'size' : 119,
        'div' : 20,
        'sections' : [[0,0],[119,0],[119,119],[0,119]]
    },    
    # One section -- the entire display
    'BIG' : {
        'xofs' : 0,
        'yofs' : 0,
        'size' : 239,
        'div' : 30,
        'sections' : [[0,0]]
    }
    # Others ... maybe 3x3 or 4x4? Maybe BIG at smaller sizes/offsets?
}

# Some default colors
DEFAULT_COLORS = [
    0x000000, # 0
    
    0xFFFFFF, # 1 White
    0xFF0000, # 2 Red
    0x00FF00, # 3 Green
    0x0000FF, # 4 Blue    
    
    0x008000, # 5 Dark green    
    ]

for x in range(len(DEFAULT_COLORS)):
    color_palette[x] = DEFAULT_COLORS[x]

# The display script

SCRIPT = [
    'Color 0=0', 
    'Color 1=008000', 
    'Color 2=FFFFFF',
    
    'Config BIG',
    'Draw 0A.1+0B+0C+0D',
    'Sleep 2',
    'Clear UNDO',
    
    'Config FOUR',    
    'Draw 0A.1+1B+2C+3D',
    'Draw 0C.2+1D+2A+3B',
    'Sleep 5',
    'Clear UNDO'
]

# Run the script (repeatedly)

artist = LineArt(line,color_bitmap,color_palette,CONFIGS)

while True:
    artist.run_commands(SCRIPT)
