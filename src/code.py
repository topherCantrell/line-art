# Circuit Python

from hardware_gizmo import HardwareGizmo
from line_art import LineArt

hardware = HardwareGizmo()

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
    hardware.set_color(x,DEFAULT_COLORS[x])

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

artist = LineArt(hardware,CONFIGS)

while True:
    artist.run_commands(SCRIPT)
