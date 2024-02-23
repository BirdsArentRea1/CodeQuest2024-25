cases = int(input().rstrip())
abc = 0
for i in range(cases):
    line = input().rstrip()
    
    for j in line:
        if j == 'a' or 'b':
            abc +=1
    print(abc+1)
    abc = 0
