cases = int(input().rstrip())
R = 0 #Rock
P = 0 #Paper
S = 0 #Scissors
X = 0 #No Winner

for i in range(cases):
    line = input().rstrip()

    for j in line:
        if (j == 'R','P'):
            P +=1
        elif (j == 'R','S'):
            R +=1
        elif (j == 'P','S'):
            S +=1
        elif (j == 'R','P','S'):
            X +=1
        elif (j == 'R','R'):
            X +=1

    if (R > P and R > S and R > X):
        print("ROCK")
    elif (P > R and P > S and P > X):
        print("PAPER")
    elif (S > R and S > P and S > X):
        print("SCISSORS")
    elif (X > R and X > P and X > S):
        print("NO WINNER")
     
