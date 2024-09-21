import math

s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
     5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
     6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

# Left rotate function
def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

# Padding the message to 512-bit blocks
def md5_padding(message):
    message_byte_array = bytearray(message, 'utf-8')
    original_length_bits = (8 * len(message_byte_array)) & 0xFFFFFFFFFFFFFFFF
    message_byte_array.append(0x80)

    while len(message_byte_array) % 64 != 56:
        message_byte_array.append(0)

    message_byte_array += original_length_bits.to_bytes(8, byteorder='little')
    return message_byte_array

# MD5 main function
def md5(message):
    message = md5_padding(message)
    
    # Initialize variables:
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    for chunk_offset in range(0, len(message), 64):
        a, b, c, d = A, B, C, D
        chunk = message[chunk_offset:chunk_offset + 64]
        M = [int.from_bytes(chunk[i:i+4], byteorder='little') for i in range(0, 64, 4)]

        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            elif 48 <= i <= 63:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
            a = d
            d = c
            c = b
            b = (b + left_rotate(f, s[i])) & 0xFFFFFFFF

        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Produce the final hash value (digest)
    return ''.join(format(x, '02x') for x in A.to_bytes(4, byteorder='little') +
                   B.to_bytes(4, byteorder='little') +
                   C.to_bytes(4, byteorder='little') +
                   D.to_bytes(4, byteorder='little'))

input_string = "Hello, world!"
md5_result = md5(input_string)

print(f"MD5 hash of '{input_string}' is: {md5_result}")