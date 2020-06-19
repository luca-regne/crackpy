from ..code import toBinary, toAscii

def xor(message, key):
    message_bin = toBinary.ascii(message)
    key = list(key)
    while len(message_bin) > len(key):
        key.insert(0, '0')

    for i in range(len(message_bin)):
        if message_bin[i] == key[i]:
            message_bin[i] =  '0'
        else:
            message_bin[i] = '1'

    return ''.join(message_bin)