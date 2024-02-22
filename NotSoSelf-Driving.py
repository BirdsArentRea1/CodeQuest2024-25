import sys

cases =  int(sys.stdin.readline().rstrip())

for testcases in range(cases):
        line = sys.stdin.readline().rstrip()
        s, d = (float(val) for val in line.split(":"))
    
        if s > 0:
            t = d / s
            if t <= 1:
                print("SWERVE")
            elif t <= 5:
                print("BRAKE")
            else:
                print("SAFE")
        else:
            print("SAFE")
            
#speed = s, distance = d, time = t, 
