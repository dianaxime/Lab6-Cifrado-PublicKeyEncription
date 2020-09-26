'''
Maria Jose Castro 181202
Diana de Leon 18607
Camila Gonzalez 18398
Maria Ines Vasquez 18250
'''
import socket
import rsa

#instanciamos la conexion
s = socket.socket()
#indicamos el puerto
s.connect(("127.0.0.1", 9999))
# Generar llaves propias
rsa.arch_key(10, "cli")
publicServ = rsa.get_key('servpub.key')
privateCli = rsa.get_key('clipriv.key')

while True:
    #se le pide al usuario ingresar el mensaje
    mensaje = input(" Ingresa Mensaje: ")
    #utiliza la llave publica del servidor para cifrar el mensaje
    publicServ = rsa.get_key('servpub.key')
    s.send(bytes(rsa.cifrar(mensaje, publicServ),'utf-8'))
    print("Mensaje encriptado enviado: %s" %
          (str(rsa.cifrar(mensaje, publicServ))))
    if mensaje == "quit":
        break

print("adios")

s.close()
