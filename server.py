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
s.bind(("127.0.0.1", 9999))
s.listen(1)  
sc, addr = s.accept() 
#generar llaves propias 
rsa.arch_key(10, "serv")
public = rsa.get_key('servpub.key')
private = rsa.get_key('servpriv.key')
#Mientras el mensaje sea distindo de quit que continue 
# con el proceso de recibir y enviar mensajes
while True:  
      recibido = sc.recv(1024)  
      if recibido == "quit":  
         break        
      print("Mensaje Encriptado Recibido: ", recibido.decode('utf-8'))
      #Se llama a la funcion de descifrado para mostrar el mensaje
      print("Mensaje Desencriptado: %s" %(rsa.decifrar(recibido.decode('utf-8'), private)))
      sc.send(recibido)  
  
print("adios")  
  
sc.close()  
s.close() 