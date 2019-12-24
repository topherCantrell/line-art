# Circuit Python

from hardware_gizmo import HardwareGizmo
from line_art import LineArt

hardware = HardwareGizmo()

# A few section configurations for the gizmo hardware

from SCRIPT_Christmas_2019 import SCRIPT
from SCRIPT_Christmas_2019 import DEFAULT_COLORS
from SCRIPT_Christmas_2019 import CONFIGS

for x in range(len(DEFAULT_COLORS)):
    hardware.set_color(x,DEFAULT_COLORS[x])

# Run the script (repeatedly)

artist = LineArt(hardware,CONFIGS)

while True:
    artist.run_commands(SCRIPT)
