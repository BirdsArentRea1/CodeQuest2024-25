cases = int(input().rstrip())
LetterScore = 0

for i in range(cases):
    line = input().rstrip()

    for j in line:
        if j in {'A','E','I','L','N','O','R','S','T','U'}:
            print(f"{j}=1")
            LetterScore += 1
        if j in ('D','G'):
            print(f"{j}=2")
            LetterScore +=2
        if j in ('B','C','M','P'):
            print(f"{j}=3")
            LetterScore += 3
        if j in ('F','H','V','W','Y'):
            print(f"{j}=4")
            LetterScore += 4
        if j == 'K':
            print(f"{j}=5")
            LetterScore += 5
        if j in ('J','X'):
            print(f"{j}=8")
            LetterScore += 8
        if j in ('Q','Z'):
            print(f"{j}=10")
            LetterScore += 10

    print(f"Total={LetterScore}")

# points_per_letter:dict = {
#     "1": ['A','E','I','L','N','O','R','S','T','U'],
#     "2": ['D','G'],
#     "3": ['B','C','M','P'],
#     "4": ['F','H','V','W','Y'],
#     "5": ['K'],
#     "8": ['J','X'],
#     "10": ['Q','Z'], 
#     }
        

# for item in dict:
#     if dict(item) == 'A':
#         print (dict(item))

