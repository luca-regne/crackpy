from ..code import toBinary, toAscii

def xor(message, key):
    message = list(message)
    key = list(key)
    
    while len(message) > len(key):
        key.insert(0, '0')

    for i in range(len(message)):
        if message[i] == key[i]:
            message[i] =  '0'
        else:
            message[i] = '1'

    print(''.join(message))