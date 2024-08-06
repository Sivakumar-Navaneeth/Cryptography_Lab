def generate_playfair_key_matrix(key):
    """Generates the key matrix using the given key."""

    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(sorted(set(key), key=key.index))  # Remove duplicates, maintain order
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def preprocess_text(text):
    """Preprocesses the given text by converting J to I and splitting into pairs of twos."""

    text = text.upper().replace("J", "I")
    processed_text = ""
    i = 0
    while i < len(text):
        processed_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += "X"
        elif i + 1 < len(text):
            processed_text += text[i + 1]
            i += 1
        i += 1
    if len(processed_text) % 2 != 0:
        processed_text += "X"
    return processed_text

def find_position(matrix, char):
    """Finds the position of a character in the key matrix."""

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    """Encrypts the given text using the Playfair Cipher with the specified key matrix."""

    matrix = generate_playfair_key_matrix(key)
    print(matrix)
    plaintext = preprocess_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    """Decrypts the given text using the Playfair Cipher with the specified key matrix."""

    matrix = generate_playfair_key_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            plaintext += matrix[row_a][(col_a - 1) % 5]
            plaintext += matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            plaintext += matrix[(row_a - 1) % 5][col_a]
            plaintext += matrix[(row_b - 1) % 5][col_b]
        else:
            plaintext += matrix[row_a][col_b]
            plaintext += matrix[row_b][col_a]
    return plaintext

text = input("Enter Text: ")
key = input("Enter Key: ").upper()
    
result = playfair_encrypt(text, key)
print("CipherText: ", result)
result = playfair_decrypt(result, key)
print("PlainText: ", result)
