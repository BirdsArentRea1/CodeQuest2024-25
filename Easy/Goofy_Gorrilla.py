import sys

cases = int(input().rstrip())
for i in range (cases):
    line = sys.stdin.readline().rstrip()
    line = line.split(" ")
     
    if line[0] == 'true' and line[1]== 'true':
        print("true")
    else:
        print("false")
