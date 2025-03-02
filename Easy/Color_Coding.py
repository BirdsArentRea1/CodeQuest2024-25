cases = int(input().rstrip())

for i in range(cases):
    line = input().rstrip()
    if 'red' in line:
        print("red")
    elif 'blue' in line:
        print("blue")
    elif 'blue''red' not in line:
        print("no color found")
