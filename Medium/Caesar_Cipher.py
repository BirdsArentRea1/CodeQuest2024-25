def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

num_inputs = int(input())

for _ in range(num_inputs):
    shift_value = int(input())
    ciphered_message = input()
    decrypted_message = caesar_cipher(ciphered_message, -shift_value)
    print(decrypted_message)
