from ..code.toBinary import asciiToBinary

def xor (message, key):
    message = list(message)
    key = list(key)

    x = len(key)
    while len(message) > len(key):
        key.append(key[ len(key) - x])

    message = ''.join(message)
    key = ''.join(key)

    message_bin = asciiToBinary(message)
    key_bin = asciiToBinary(key)

    print('message: {}'.format(message_bin))
    print('key: {}'.format(key_bin))

    for i in range(len(message_bin)):
        if message_bin[i] == key_bin[i]:
            message_bin[i] =  0

    return(message_bin)