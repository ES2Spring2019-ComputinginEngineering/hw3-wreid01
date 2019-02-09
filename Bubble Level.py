#Name: Will Reid
#Partner: Daniel Nguyen

import microbit
import math

def angleConverter(theta):
    ang = theta * (360/(2*math.pi))
    print(ang)
    return ang

while True:
    microbit.sleep(200)

    z = (microbit.accelerometer.get_z())

    y = (microbit.accelerometer.get_y())

    x = (microbit.accelerometer.get_x())

    #Y axis
    def getYangle():
        d = x*x + z*z
        f = y / math.sqrt(d)
        Ay = math.atan(f)
        return Ay

    #X Axis
    def getXangle():
        d = y*y + z*z
        f = x / math.sqrt(d)
        Ax = math.atan(f)
        return Ax

    xTilt = angleConverter(getXangle())
    yTilt = angleConverter(getYangle())


    print((x, y, z))

    if xTilt < -10:
        if yTilt > 10:
            from microbit import *
            display.show(Image.ARROW_SW)
        elif yTilt < -10:
            from microbit import *
            display.show(Image.ARROW_NW)
        else:
            from microbit import *
            display.show(Image.ARROW_W)
    elif xTilt > 10:
        if yTilt > 10:
            from microbit import *
            display.show(Image.ARROW_SE)
        elif yTilt < -10:
            from microbit import *
            display.show(Image.ARROW_NE)
        else:
            from microbit import *
            display.show(Image.ARROW_E)
    elif xTilt > -10 and xTilt < 10:
        if yTilt > 10:
            from microbit import *
            display.show(Image.ARROW_S)
        elif yTilt < -10:
            from microbit import *
            display.show(Image.ARROW_N)
        else:
            from microbit import *
            display.show(Image.TARGET)