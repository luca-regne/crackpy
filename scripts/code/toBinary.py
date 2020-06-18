def asciiToBinary(ascii):
    byte_array = ascii.encode()
    binary_int = int.from_bytes(byte_array, 'big')
    binario = list(bin(binary_int))
    
    binario.remove('b')

    for i in range(len(binario)): 
        if binario[i] == '0':
            binario[i] = 0
        else:
            binario[i] = 1


    return(binario)