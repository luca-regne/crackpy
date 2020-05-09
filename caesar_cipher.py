message = list(str(input('Informe a mesagem: ')))
number = []

converter = list('abcdefghijklmnopqrstuvwxyz')

for m in message:
    number.append(converter.index(m))

for x in range(26):
    message_decrypt = ''
    for i in range(len(number)):
        message_decrypt += converter[(number[i]+x)]
    print("rotação +{} --> {}".format(x, message_decrypt))