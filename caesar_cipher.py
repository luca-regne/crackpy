def caesar_cipher(message, rotation = 0):
    number = []
    converter = list('abcdefghijklmnopqrstuvwxyz')

    for m in message:
        number.append(converter.index(m))

    if rotation != 0:
        message_decrypt = ''
        for i in range(len(number)):
            x = (number[i]+rotation)%26
            message_decrypt += converter[x]
            message_decrypt += converter[(number[i]+rotation)]
        print("rotação +{} --> {}".format(rotation, message_decrypt))

    else: 
        for rotation in range(26):
            message_decrypt = ''
            for i in range(len(number)):
                x = (number[i]+rotation)%26
                message_decrypt += converter[x]
            print("rotação +{} --> {}".format(rotation, message_decrypt))