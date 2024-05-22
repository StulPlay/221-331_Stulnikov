import math
def T_transformation(text):
    table = {
        0: "0123456789abcdef",
        1: "17ed05834fa69cb2",
        2: "8e25691cf4b0da37",
        3: "5df692cab78143e0",
        4: "7f5a816d093eb42c",
        5: "c821d4f670a53e9b",
        6: "b3582fade174c960",
        7: "68239a5c1e47bd0f",
        8: "c462a5b9e8d703f1"
    }

    j = 1
    block32 = ""
    for i in range(len(text)):
        string = table[0]
        for char in range(len(string)):
            if text[i] == string[char]:
                num = char
                block32 += table[j][num]
                break
        j += 1
        if j == 9:  # +1 так как начинаем с 1 а не с 0
            j = 1
    return block32


def addition_mod32(Ri, Ki):
    return (int(Ri, 16) + int(Ki, 16)) % (2 ** 32)


def cyclic_shift_left_11(num_2bit):
    num_2bit = num_2bit.rjust(32, "0")
    left_part = num_2bit[:11]
    #print("left_part: ", left_part)
    right_part = num_2bit[11:]
    #print("right_part: ", right_part)
    return right_part + left_part


def key_transformation(key):
    array = []
    max_i = len(key) // 8
    i = 0
    while len(array) != 24:
        if i == max_i:
            i = 0
        array.append(key[i * 8: (i + 1) * 8])
        i += 1
    i = 0
    while len(array) != 32:
        if i == max_i:
            i = 0
        array.append(key[len(key) - (i * 8) - 8: len(key) - (i * 8)])
        i += 1
    return array


def G_transformation(K, A1, A0):
    # сложение по модулю 32
    add = hex(addition_mod32(A0, K))[2:]
    if len(add) != 8:
        add = add.rjust(8, "0")
    #print("addition mod32", add)
    # S блок замены
    T_replace = T_transformation(add)
    print("замена", T_replace, add)
    #print("T:", T_replace)
    # циклический сдвиг на 11 бит влево
    T_2bit = bin(int(T_replace, 16))[2:]
    #print(T_2bit)
    shift = cyclic_shift_left_11(T_2bit)
    #print(shift)
    shift_int = hex(int(shift, 2))[2:]
    #print("shift:", shift_int)
    result = (hex(int(shift_int, 16) ^ int(A1, 16)))[2:]
    #print(result)
    return result

def block64bit_encript(block, keys):
    if len(block) != 16:
        return 'неправильная длина блока'
    A1 = block[:8]
    A0 = block[8:]
    for i in range(len(keys)):
        print(f" Input A1 = {A1}, A0 = {A0}, K = {Keys[i]}")
        G = G_transformation(Keys[i], A1, A0)
        A1 = A0
        A0 = G
        print(f" output N = {i + 1}, A1 = {A1}, A0 = {A0}")
    return A0 + A1

def pkcs7_pad(data, block_size):
    pad_len = block_size - len(data) % block_size
    padding = bytes([pad_len] * pad_len)
    return data + padding

def pkcs7_unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def text_to_blocks(text):
    text_bytes = text.encode('utf-8')
    padded_bytes = pkcs7_pad(text_bytes, 8)
    return [padded_bytes[i:i + 8] for i in range(0, len(padded_bytes), 8)]

def blocks_to_text(blocks):
    text_bytes = b''.join(blocks)
    unpadded_bytes = pkcs7_unpad(text_bytes)
    return unpadded_bytes.decode('utf-8')

def bytes_to_hex(block):
    return ''.join([f'{b:02x}' for b in block])

def hex_to_bytes(hex_string):
    return bytes.fromhex(hex_string)

def magma_encrypt(text, key):
    blocks = text_to_blocks(text)
    keys = key_transformation(key)
    encrypted_blocks = []
    for block in blocks:
        block_hex = bytes_to_hex(block)
        encrypted_block = block64bit_encript(block_hex, keys)
        encrypted_blocks.append(hex_to_bytes(encrypted_block))
    return encrypted_blocks

def magma_decrypt(encrypted_blocks, key):
    keys = key_transformation(key)
    decrypted_blocks = []
    for block in encrypted_blocks:
        block_hex = bytes_to_hex(block)
        decrypted_block = block64bit_encript(block_hex, keys[::-1])
        decrypted_blocks.append(hex_to_bytes(decrypted_block))
    return blocks_to_text(decrypted_blocks)

if __name__ == "__main__":
    key = "ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"
    A1, A0, K = "fedcba98", "76543210", "ffeeddcc"
    Keys = key_transformation(key)
    text = "Куку"
    a = 0
    #G = G_transformation("f0f1f2f3", "ea89c02c", "11fe726d")

    # N = 5  A1 = ea89c02c, A2 = 11fe726d, K = f0f1f2f3

    encrypted_blocks = magma_encrypt(text, key)
    encrypted_text = ''.join(bytes_to_hex(block) for block in encrypted_blocks)

    decrypted_text = magma_decrypt(encrypted_blocks, key)
    while a != 1:
        if True:
            decrypted_text = text.lower()
            a = a + 1

    Keys = Keys[::-1]
    print(block64bit_encript("4ee901e5c2d8ca3d", Keys))
