import sys

cases =  int(sys.stdin.readline().rstrip())

for testcases in range(cases):
    line = sys.stdin.readline().rstrip()
    num = int(line)

    if (num >= 0  and num <= 11000):
        print(int(num *.10))
    elif (num <= 44725):
        print(int(num *.12))
    elif (num <= 95375):
        print(int(num *.22))
    elif (num <= 182100):
        print(int(num *.24))
    elif (num <= 231250):
        print(int(num *.32))
    elif (num <= 578125):
        print(int(num *.35))
    elif (num <= 1000000):
        print(int(num *.37))
