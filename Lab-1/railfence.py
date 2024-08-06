def encrypt_rail_fence(text, key):
    """Encrypts the given text using the Rail Fence Cipher with the specified key."""

    rail = [[] for _ in range(key)]
    direction = 1
    row = 0

    for char in text:
        rail[row].append(char)
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    ciphertext = ''.join(''.join(row) for row in rail)
    return ciphertext
 
def decrypt_rail_fence(ciphertext, key):
    """Decrypts the given ciphertext using the Rail Fence Cipher with the specified key."""

    rail = [[] for _ in range(key)]
    direction = 1
    row = 0

    for _ in ciphertext:
        rail[row].append('*')
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    index = 0
    for i in range(key):
        for j in range(len(rail[i])):
            if rail[i][j] == '*':
                rail[i][j] = ciphertext[index]
                index += 1

    plaintext = ''
    row = 0
    direction = 1
    for _ in ciphertext:
        plaintext += rail[row].pop(0)
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1
        row += direction

    return plaintext

plaintext = input("Enter PlainText: ")
key = int(input("Enter Key: "))

encrypted_text = encrypt_rail_fence(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt_rail_fence(encrypted_text, key)
print("Decrypted text:", decrypted_text)