def rail_fence_encrypt(text, rails):
    # Remove spaces for cleaner encryption
    text = text.replace(" ", "")

    # Create empty rails
    fence = [""] * rails

    direction_down = False
    row = 0

    # Place characters in zig-zag
    for char in text:
        fence[row] += char

        # Change direction at top or bottom
        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        # Move row up or down
        row += 1 if direction_down else -1

    # Read rails row by row
    return "".join(fence)

## decryption code
def rail_fence_decrypt(cipher, rails):
    # Create matrix filled with '\n'
    fence = [["\n" for _ in range(len(cipher))] for _ in range(rails)]

    direction_down = None
    row, col = 0, 0

    # Step 1: Mark zig-zag positions with '*'
    for i in range(len(cipher)):
        fence[row][col] = "*"

        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False

        row += 1 if direction_down else -1
        col += 1

    # Step 2: Fill cipher text row-wise
    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if fence[r][c] == "*" and index < len(cipher):
                fence[r][c] = cipher[index]
                index += 1

    # Step 3: Read text in zig-zag order
    result = []
    row, col = 0, 0

    for i in range(len(cipher)):
        result.append(fence[row][col])

        if row == 0:
            direction_down = True
        elif row == rails - 1:
            direction_down = False

        row += 1 if direction_down else -1
        col += 1

    return "".join(result)


## Example code
message = "HELLO WORLD"
rails = 3

encrypted = rail_fence_encrypt(message, rails)
print("Encrypted:", encrypted)

decrypted = rail_fence_decrypt(encrypted, rails)
print("Decrypted:", decrypted)

### OUTPUT
Encrypted: HOLELWRDLO
Decrypted: HELLOWORLD

