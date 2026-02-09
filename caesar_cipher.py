def caesar_cipher(text, shift):
    result = ""

    for char in text:

        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        # Keep spaces, numbers, symbols unchanged
        else:
            result += char

    return result


## example code
message = "hello world"
shift = 3
encpt = caesar_cipher(message, shift)
print("Encrypted: ", encpt)
dcpt = caesar_cipher(encpt, -1 * shift)
print("Decrypted:", dcpt)


### OUTPUT
Encrypted:  khoor zruog
Decrypted: hello world
