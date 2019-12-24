from hardware_pc import HardwarePC
from line_art import LineArt

hardware = HardwarePC()

from SCRIPT_Christmas_2019 import SCRIPT
from SCRIPT_Christmas_2019 import DEFAULT_COLORS
from SCRIPT_Christmas_2019 import CONFIGS

for x in range(len(DEFAULT_COLORS)):
    hardware.set_color(x,DEFAULT_COLORS[x])

artist = LineArt(hardware,CONFIGS)

#while True:
artist.run_commands(SCRIPT)
