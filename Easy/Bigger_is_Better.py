cases = int(input().rstrip())

for i in range(cases):
    
    max_gus = 0
    
    scores = input().strip().split(' ')
    scores = [int(val) for val in scores]
    
    for i in range(len(scores)):
        if scores[i] > scores[max_gus]:
            max_gus = i
            
    print(scores[max_gus])
