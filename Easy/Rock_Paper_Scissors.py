import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = input().rstrip()
    Rock = False
    Paper = False
    Scissors = False
    line = sys.stdin.readline().rstrip()
    for charactor in line:
        if charactor == 'R':
            Rock = True
        if charactor == 'P':
            Paper = True
        if charactor == 'S':
            Scissors = True

    if Rock and Paper and Scissors:
        print("NO WINNER")
    elif Rock and Paper:
        print("PAPER")
    elif Paper and Scissors:
        print("SCISSORS")
    elif Rock and Scissors:
        print("ROCK")    
