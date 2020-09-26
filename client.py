import socket
import rsa

s = socket.socket()
s.connect(("127.0.0.1", 9999))
# Generar llaves propias
rsa.arch_key(10, "cli")
publicServ = rsa.get_key('servpub.key')
privateCli = rsa.get_key('clipriv.key')
while True:
    mensaje = input(" Ingresa Mensaje: ")
    publicServ = rsa.get_key('servpub.key')
    s.send(bytes(rsa.cifrar(mensaje, publicServ),'utf-8'))
    print("Mensaje encriptado enviado: %s" %
          (str(rsa.cifrar(mensaje, publicServ))))
    if mensaje == "quit":
        break

print("adios")

s.close()
