def caesar_cipher(message, rotation):
    message = message.lower()
    number = []
    output = ''
    converter = list('abcdefghijklmnopqrstuvwxyz')
    if rotation < 0:
        rotation += 26

    for m in message:
        number.append(converter.index(m))

    if rotation !=0:
        message_decrypt = ''
        for i in range(len(number)):
            x = (number[i]+rotation)%26
            message_decrypt += converter[x]
        output += "rotação +{} --> {}\n".format(rotation, message_decrypt)

    else: 
        for rotation in range(26):
            message_decrypt = ''
            for i in range(len(number)):
                x = (number[i]+rotation)%26
                message_decrypt += converter[x]
            output += "rotação +{} --> {}\n".format(rotation, message_decrypt)

    return(output)