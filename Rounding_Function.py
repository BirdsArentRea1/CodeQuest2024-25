import math
#round 1.355 to 2nd decimal
    
def round(val, dec):
    if val < 0:
        negative = True
    else:
        negeative = False
            
    absoluteVal = abs(val)
        
    absoluteVal = absoluteVal * 10**(dec)
        
    remainder = (absoluteVal *10) %10
        
    if remainder >= 5:
        roundedVal = math.ceil(absoluteVal)
    else:
        roundedVal = math.floor(absoluteVal)
    return roundedVal/(10**dec)
        
print(round(1.355, 2))
