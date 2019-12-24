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

    
    
C_Black = '000000'
C_White = 'FFFFFF'
C_Silver = 'C0C0C0'
C_Gray = '808080'
C_Red = 'FF0000'
C_Maroon = '800000'
C_Yellow = 'FFFF00'
C_Olive = '808000'
C_Lime = '00FF00'
C_Green = '008000'
C_Aqua = '00FFFF'
C_Teal = '008080'
C_Blue = '0000FF'
C_Navy = '000080'
C_Fuchsia = 'FF00FF'
C_Purple = '800080'
C_Dark_Green = '002000'

# Some default colors
DEFAULT_COLORS = [    
    int(C_Black,16),   
    int(C_White,16), 
    int(C_Silver,16), 
    int(C_Gray,16), 
    int(C_Red,16), 
    int(C_Maroon,16), 
    int(C_Yellow,16), 
    int(C_Olive,16), 
    int(C_Lime,16), 
    int(C_Green,16), 
    int(C_Aqua,16), 
    int(C_Teal,16), 
    int(C_Blue,16), 
    int(C_Navy,16), 
    int(C_Fuchsia,16), 
    int(C_Purple,16), 
    int(C_Dark_Green,16),     
]

# The display script
SCRIPT = [    
    'Config FOUR',
    'Color 0='+C_Teal, 
    'Color 1='+C_Red,
    'Color 2='+C_Aqua,
    'Color 3='+C_Lime,
    'Draw 0A.1+1B+2C+3D',
    'Draw 0C.2+1D+2A+3B',
    'Draw 0D.3+1C+2B+3A',
    'Sleep 5',
    'Clear UNDO',   
    
    'Config BIG',
    'Color 0='+C_Black, 
    'Color 1='+C_Green, 
    'Color 2='+C_White,
    'Draw 0A.1+0B+0C+0D',
    'Config FOUR', 
    'Draw 0C.2+1D+2A+3B',
    'Sleep 2',
    'Clear UNDO',
    
    'Config FOUR',    
    'Draw 0A.1+1B+2C+3D',
    'Draw 0C.2+1D+2A+3B',
    'Sleep 5',
    'Clear UNDO',    
]
