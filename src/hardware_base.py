# TODO: Use ABC

import time

class HardwareBase():
    
    def __init__(self,width,height):
        self._width = width
        self._height = height
    
    def set_color(self,num,val):
        # Abstract
        pass
    
    def set_pixel(self,x,y,color):
        # Abstract
        pass
    
    def pause(self,num_sec):
        time.sleep(num_sec)
    
    def clear(self,color=0):
        for y in range(self._height):
            for x in range(self._width):
                self.set_pixel(x,y,color)
                
    def draw_line(self,x0,y0,x1,y1,color):        
        # Line drawing function.  Will draw a single pixel wide line starting at
        # x0, y0 and ending at x1, y1.
        set_pixel_fn = self.set_pixel # cache for speed
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
                set_pixel_fn(y0,x0,color)                
            else:
                set_pixel_fn(x0,y0,color)                
            err -= dy
            if err < 0:
                y0 += ystep
                err += dx
            x0 += 1