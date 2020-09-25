"""
Laboratorio 5
Cifrado de información
#Maria Jose Castro 181202
#Diana de Leon 18607
#Camila Gonzalez 18398
#Maria Ines Vasquez 18250
"""
"""Código extraído de : https://cryptobook.nakov.com/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples"""
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

#genera una nueva pareja de llave, una privada y una pública. Puede recibir parámetros como el largo en bits de la llave deseada, exponente del RSA público y función que genere bytes random
keyPair = RSA.generate(3072)

#se construye una nueva llave solamente con la información pública
pubKey = keyPair.publickey()
#se imprime el módulo y el exponente público de la public key
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
#se genera una cadena de bits con la llave pública codificada
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
#se imprime el módulo y el exponente privado de la private key
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
#se genera una cadena de bits con la llave privada codificada
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

msg = b'Esto sera facil de encriptar'
#se instancia cifrador asimétrico basado en RSA y utiliza el método de padding OAEP con la llave pública
encryptor = PKCS1_OAEP.new(pubKey)
#encripta un texto con la public key que se generó con RSA y lo devuelve como tipo byte
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))


#se instancia cifrador asimétrico basado en RSA y utiliza el método de padding OAEP con la pareja de llaves
decryptor = PKCS1_OAEP.new(keyPair)
#desencripta un texto con la pareja de keys que se generó con RSA y lo devuelve como tipo byte
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)