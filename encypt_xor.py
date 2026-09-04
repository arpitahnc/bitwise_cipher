def reverse_bits(byte):
    #convert to binary
    binary = bin(byte)
    #removing extra 1b from binary digit
    binary = binary[2:]
    #reverse binary
    reversed_binary = binary[::-1]
    return reversed_binary

#def rotate_right(byte):

def rotate_left(byte, shift):
    shift = shift % 8
    left_part = byte << shift
    right_part = byte >> (8 - shift)
    result = left_part | right_part
    result = result & 0xFF   # keep only 8 bits
    return result

def xor_bits(x,y):
    xor_text = x ^ y
    return xor_text


def encrypt(text,rotation):
    encrypted_text = ""

    for letter in text:
        original = ord(letter) #ASCII from og text
        #reverse text
        reversed_str = reverse_bits(original) 
        reversed_int = int(reversed_str,2)
        # rotate
        rotate_text = rotate_left(reversed_int, rotation)
        #xor og text and new
        numbers = xor_bits(original,rotate_text) 
        new_txt = chr(numbers)
        encrypted_text = encrypted_text + new_txt

    return encrypted_text


message = input("enter text:")
rotation = int(input("enter key:"))
encrypted = encrypt(message,rotation)
print("encrypted:",encrypted)