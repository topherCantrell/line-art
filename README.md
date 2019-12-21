# Line Art

![](art/config.jpg)

E,F,G,H are big-corners of the display (A,B,C,D).

## Panel language

`TODO: This has evolved`

A corner is described with number (quadrant), letter (corner/direction), and color (2 digit hex):

For instance, `2b03` is quadrant 2, corner B (counter-clockwise), and color 3.

A display rendering is defined by a series of corners separated by a comma ',' or plus '+'.
For instance: `1a02+3A04,1a04`

The comma menas to finish drawing before moving to the next corner. The '+' means to draw the corners
at the same time.

## Christmas 2019

For the Circuit Playground Bluefruit + TFT Gizmo

```
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
```