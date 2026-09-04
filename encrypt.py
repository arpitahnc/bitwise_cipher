def reverse_bits(byte):
    # convert number to 8-bit binary text
    binary = bin(byte)[2:].zfill(8)
    # reverse the text
    reversed_binary = binary[::-1]
    # convert back to number
    result = int(reversed_binary, 2)
    return result

def rotate_left(byte, shift):
    shift = shift % 8
    left_part = byte << shift
    right_part = byte >> (8 - shift)
    result = left_part | right_part
    result = result & 0xFF   # keep only 8 bits
    return result

def encrypt(text, rotation):
    encrypted_text = ""

    for letter in text:
        number = ord(letter)              # get ASCII number
        number = reverse_bits(number)     # reverse the bits
        number = rotate_left(number, rotation)  # rotate bits
        new_letter = chr(number)          # turn back into a character
        encrypted_text = encrypted_text + new_letter

    return encrypted_text

# --- MAIN PROGRAM ---
message = input("Enter text to encode: ")
rotation = 3

encrypted = encrypt(message, rotation)
print("Encrypted:", encrypted)