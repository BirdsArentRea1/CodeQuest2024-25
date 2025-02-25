def convert_opposite(cases):
    for i in range(len(cases)):
        if 'A' <= cases[i] <= 'Z':
            cases[i] = chr(ord(cases[i]) + 32)

if __name__ == "__main__":
    sentences = int(input())
    for _ in range(sentences):
        cases = input().rstrip()
        cases = list(cases)
        convert_opposite(cases)
        result = ''.join(cases)
        print(result)
