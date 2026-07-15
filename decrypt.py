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

def rotate_right(byte, shift):
    shift = shift % 8
    right_part = byte >> shift
    left_part = byte << (8 - shift)
    result = left_part | right_part
    result = result & 0xFF   # keep only 8 bits
    return result


def decrypt(cipher_text, rotation):
    decrypted_text = ""

    for letter in cipher_text:
        number = ord(letter)
        number = rotate_right(number, rotation)  # undo rotate
        number = reverse_bits(number)             # undo reverse
        new_letter = chr(number)
        decrypted_text = decrypted_text + new_letter

    return decrypted_text

# --- main program ---
message = input("Enter text to decode: ")
rotation = 3

decrypted = decrypt(message, rotation)
print("Decrypted:", decrypted)