from hardware_base import HardwareBase

import displayio
from adafruit_gizmo import tft_gizmo

class HardwareGizmo(HardwareBase):
    
    def __init__(self):
        super().__init__(240,240)
        self._display = tft_gizmo.TFT_Gizmo()
        self._splash = displayio.Group(max_size=10)
        self._display.show(self._splash)
        self._color_bitmap = displayio.Bitmap(240, 240, 32)
        self._color_palette = displayio.Palette(32)
        self._bg_sprite = displayio.TileGrid(self._color_bitmap, pixel_shader=self._color_palette, x=0, y=0)
        self._splash.append(self._bg_sprite)
        
    def set_color(self,num,val):
        self._color_palette[num] = val
    
    def set_pixel(self,x,y,color):
        self._color_bitmap[x,y] = color
        