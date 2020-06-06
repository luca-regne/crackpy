def vigenere(message, key):
    converter = list('abcdefghijklmnopqrstuvwxyz')

    x = len(key)
    while len(message) != x:
        key.append(key[x])
        x += 1

    for i in range(len(message)):
        message[i] = converter[ converter.index(message[i]) + converter.index(key[i]) % 26 ]
    
    return(message)