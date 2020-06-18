def vigenere(message, key):
    converter = list('abcdefghijklmnopqrstuvwxyz')
    output = ''
    x = len(key)

    while len(message) > len(key):
        key.append(key[ len(key) - x ])

    for i in range(len(message)):
        output += converter[ ( converter.index( message[i] ) + converter.index( key[i] ) ) % 26 ]
    
    print(output)
