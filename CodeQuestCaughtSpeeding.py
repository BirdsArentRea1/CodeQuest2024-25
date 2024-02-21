import sys

cases =  int(sys.stdin.readline().rstrip())

for testcases in range(cases):
        line = sys.stdin.readline().rstrip()
        s, bd = (val for val in line.split(" "))
        s = int(s)
       
        if bd == "true":
            if s <= 65:
                print("no ticket")
            elif s > 65 and s <= 85:
                print("small ticket")
            elif s > 85:
                print("big ticket")
               
        if bd == "false":
            if s <= 60:
                print("no ticket")
            elif s > 60 and s <= 80:
                print("small ticket")
            elif s > 80:
                print("big ticket")
