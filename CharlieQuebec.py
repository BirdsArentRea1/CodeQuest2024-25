
wordpairs = {
    "A": "Alpha",
   "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu",
    " ":" "
}

cases = int(input().rstrip())
    
letters = []
    
for i in range(cases):
    words = int(input().rstrip())
    for t in range (words):
        line = input().rstrip()
            
        for i in line:
             letters.append(i)
                
        for j in range(len(letters)):
            print(wordpairs[letters[j].upper()], end = "")
            if j+1<len(letters):
                if letters[j+1]!=" " and letters[j] != " ":
                    print("-", end = "")
                        
        letters.clear()
