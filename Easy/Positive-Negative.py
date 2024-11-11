import sys

cases =  int(sys.stdin.readline().rstrip())

for testcases in range(cases):
        line = sys.stdin.readline().rstrip()
        num = int(line)

        if (num < 0):
                print("NEGATIVE")
        else:
            print("POSITIVE")
