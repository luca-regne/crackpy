import argparse
from scripts.converter import toBinary
from scripts.coding import base64 
from scripts.crypto.caesar_cipher import caesar_cipher
from scripts.crypto.vigenere import vigenere
from scripts.crypto.xor import xor

parser = argparse.ArgumentParser(description='Ferramenta de descriptografia.')

parser.add_argument('MESSAGE',
                    help='A message to encrypt/decrypt')

parser.add_argument('-r', action='store', dest='ROTATION', type=int,
                    help="Rotation applied to decrypt/encrypt with algorithm of Caesar Cipher")

parser.add_argument('-v', action='store', dest='VIGENERE_KEY', type=str,
                    help="A key usage to decrypt a Vigenere Message.")

parser.add_argument('-x', action='store', dest='XOR_KEY_BINARY', type=str,
                    help='Usage to decrypt a binary message with bin key using xor decrypt (Return is a binary)')
                    
parser.add_argument('-xA', action='store', dest='XOR_KEY_ASCII', type=str,
                    help='Usage to decrypt a ascii message with bin key using xor decrypt (Return is a binary)')

parser.add_argument('-b64', action='store_true', 
                    help='Deconding base64 message to ascii value')

arguments = parser.parse_args()

message = arguments.MESSAGE

if arguments.b64 :
    if message[-1] + message[-2] == '==':
        message = base64.fromBase64(message)
    else:
        message = base64.toBase64(message)

if arguments.ROTATION != None:
    message = caesar_cipher(message, arguments.ROTATION)
elif arguments.VIGENERE_KEY != None:
    message = vigenere(message, list(arguments.VIGENERE_KEY))
elif arguments.XOR_KEY_BINARY != None:
    message = xor(message, arguments.XOR_KEY_BINARY)
elif arguments.XOR_KEY_ASCII != None:
    message = xor(message, toBinary.fromAscii(arguments.XOR_KEY_ASCII))

print(message)