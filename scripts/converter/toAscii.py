def fromBinary(binary):
    binary_int = int(binary, 2)
    byte_number = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_number, "big")
    text = binary_array.decode()

    return(text)
    