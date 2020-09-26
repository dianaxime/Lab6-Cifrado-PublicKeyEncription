import socket  
import rsa
 

s = socket.socket()   
s.bind(("127.0.0.1", 9999))  
s.listen(1)  
sc, addr = s.accept() 
#generar llaves propias 
rsa.arch_key(10, "serv")
public = rsa.get_key('servpub.key')
private = rsa.get_key('servpriv.key')
while True:  
      recibido = sc.recv(1024)  
      if recibido == "quit":  
         break        
      print("Mensaje Encriptado Recibido: ", recibido.decode('utf-8'))
      print("Mensaje Desencriptado: %s" %(rsa.decifrar(recibido.decode('utf-8'), private)))
      sc.send(recibido)  
  
print("adios")  
  
sc.close()  
s.close() 