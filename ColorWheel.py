cases = int(input().rstrip())

for i in range(cases):
    line = input().rstrip()
    
    if line == "yellow" or line == "red" or line == "blue":
        print("No colors need to be mixed to make", line + ".")
    elif line == "violet" or line == "blue-violet" or line == "red-violet":
        print("In order to make", line + ", blue and red must be mixed.")
    elif line == "blue-green" or line == "green" or line == "yellow-green":
        print("In order to make", line + ", blue and yellow must be mixed.")
    elif line == "yellow-orange" or line == "orange" or line == "red-orange":
        print("In order to make", line + ", red and yellow must be mixed.")
   
