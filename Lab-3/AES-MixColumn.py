def mix_columns(state):
    # Define the fixed matrix for MixColumns operation
    matrix = [[0x02, 0x03, 0x01, 0x01],
              [0x01, 0x02, 0x03, 0x01],
              [0x01, 0x01, 0x02, 0x03],
              [0x03, 0x01, 0x01, 0x02]]

    # Create a new state matrix to store the result
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    # Perform the MixColumns operation
    for col in range(4):
        for row in range(4):
            new_state[row][col] = (
                multiply(matrix[row][0], state[0][col]) ^
                multiply(matrix[row][1], state[1][col]) ^
                multiply(matrix[row][2], state[2][col]) ^
                multiply(matrix[row][3], state[3][col])
            )

    return new_state

def multiply(a, b):
    # Multiply two numbers in GF(2^8) using the AES polynomial x^8 + x^4 + x^3 + x + 1
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B
        b >>= 1
    return result

# Test the MixColumns operation
state = [
    [0xdb, 0x13, 0x53, 0x45],
    [0xf2, 0x0a, 0x22, 0x5c],
    [0x01, 0x01, 0x01, 0x01],
    [0xc6, 0xc6, 0xc6, 0xc6]
]
print('Before MixColumns:')
for i in range(4):
    print(' '.join(f'{state[i][j]:02x}' for j in range(4)))

print('\nAfter MixColumns:')
new_state = mix_columns(state)
for i in range(4):
    print(' '.join(f'{new_state[i][j]:02x}' for j in range(4)))