from ..converter import toBinary
from ..converter import toAscii

base64 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')

def toBase64(message):   
    message = list(toBinary.fromAscii(message))
    array_bit = list()
    output = ''
    size = round(len(message) / 6 + 0.4)

    for i in range(size):
        array_bit.append('')

    x = -1
    for i in range(len(message)):
        if i % 6 == 0:
            x += 1
        array_bit[x] += ''+message[i]
    
    while len(array_bit[-1]) != 6:
        array_bit[-1] += '0'

    for i in range(len(array_bit)):
        array_bit[i] = int(('00' + array_bit[i]), 2)
        output += base64[array_bit[i]] + ''
    
    output += '=='

    return output

def fromBase64(message):
    array_bit = list()
    bits = ''
    output = ''
    message = message[:-2]

    for i in range(len(message)):
        number = base64.index(message[i])
        binary = ('{0:b}'.format(number))
        while len(binary) < 6:
            binary = '0'+binary 
        bits += binary

    size = round(len(bits)/8 + 0.4)

    while len(bits) <= size*8:
        bits += '0'

    for i in range(size):
        array_bit.append('')
        for x in range(8):
            array_bit[i] += bits[ x + i*8 ]
        output += toAscii.fromBinary(array_bit[i])[-1]

    return output
