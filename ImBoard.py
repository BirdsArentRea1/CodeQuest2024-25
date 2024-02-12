cases = int(input().rstrip())
for i in range(cases):
    line = int(input().rstrip())
    for i in range(line):
        for j in range(line):
            print("#", end = "")
            if j<line-1:
                print(" ", end = "")
        print()
