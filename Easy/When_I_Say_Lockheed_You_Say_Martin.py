cases = int(input().rstrip())

for _ in range(cases):
    line = int(input())
    
    if line % 3 == 0 and line % 7 == 0:
        print("LOCKHEEDMARTIN")
    elif line % 3 == 0:
        print("LOCKHEED")
    elif line % 7 == 0:
        print("MARTIN")

    else:
        print(line)
