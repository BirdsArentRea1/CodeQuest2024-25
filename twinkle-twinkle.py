#https://lmcodequestacademy.com/problem/twinkle-twinkle
import math
import difflib
EXPECTED_OUTPUT = "0.00,100.00 -29.39,40.45 -95.11,30.90 -47.55,-15.45 -58.78,-80.90 0.00,-50.00 58.78,-80.90 47.55,-15.45 95.11,30.90 29.39,40.45"

def round(val, dec):
    if val < 0:
        negative = True
    else:
        negative = False
            
    absoluteVal = abs(val)
        
    absoluteVal = absoluteVal * 10**(dec)
        
    remainder = (absoluteVal *10) %10
        
    if remainder >= 5:
        roundedVal = math.ceil(absoluteVal)
    else:
        roundedVal = math.floor(absoluteVal)
    returnval = roundedVal/(10**dec) * (-1 if negative else 1)
    if returnval == -0:
        returnval = 0
    return returnval

cases = int(input())
for _ in range(cases):
    coordinatelist=[]
    line = input()
    centerX,centerY, pointCount, outsideRad,insideRad, = (float(val) for val in line.split(" "))
    pointCount = int(pointCount)
    for i in range(pointCount*2):
        theta = (2 * math.pi) * (i / (pointCount*2)) +math.pi/2
        theta %= (2 * math.pi)
        if i%2 != 0:
            coordinate = (insideRad*math.cos(theta)+centerX, insideRad*math.sin(theta)+centerY)

        else:
            coordinate = (outsideRad*math.cos(theta)+centerX, outsideRad*math.sin(theta)+centerY)
        coordinatelist.append(f"{round(coordinate[0], 2):0.2f},{round(coordinate[1], 2):0.2f}")
    output = (" ".join(coordinatelist))
    print(output)
