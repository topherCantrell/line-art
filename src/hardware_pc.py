import png
from hardware_base import HardwareBase

def make_png(data, colors, pixel_size, fname):
    img = []
    for y in range(len(data)):
        for yy in range(pixel_size):
            row = ()
            for x in range(len(data[y])):
                for xx in range(pixel_size):
                    row = row + colors[data[y][x]]
            img.append(row)
    with open(fname, 'wb') as f:
        w = png.Writer(len(data[0]) * pixel_size, len(data) * pixel_size, greyscale=False)
        w.write(f, img)
        
class HardwarePC(HardwareBase):
    
    def __init__(self):
        super().__init__(240,240)
        self._colors = [0] * 256
        self._pixels = []
        for _ in range(240):
            self._pixels.append([0]*240)
        self._name_index = 0
                
    def set_color(self,num,val):
        b = val&255
        g = (val>>8)&255
        r = (val>>16)&255
        self._colors[num] = (r,g,b)
    
    def set_pixel(self,x,y,color):
        self._pixels[y][x] = color
            
    def pause(self,_num_sec):
        make_png(self._pixels,self._colors,1,'LineArt'+str(self._name_index)+'.png')
        self._name_index += 1
        