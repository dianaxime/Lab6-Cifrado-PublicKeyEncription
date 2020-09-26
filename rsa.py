'''
Maria Jose Castro 181202
Diana de Leon 18607
Camila Gonzalez 18398
Maria Ines Vasquez 18250
''' 

#!/usr/bin/python
from sys import argv
import math
from random import choice
from Crypto.Util import *
from Crypto.Util.number import getPrime
from Crypto.Random import get_random_bytes

MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

def E(m, public):
    print(m, public)
    return m ** public[0] % public[1]

def D(c, private):
    print(c, private)
    return c ** private[0] % private[1]

#Aqui utilizamos el mensaje y la llave publica
#para poder cifrar el mensaje, se recorre letra por letra
#Convertimos cada letra en su numero correspondiente a ASCII
def cifrar(m, public):
    print('mensaje',m)
    chipertext = ''
    for c in m:
        print('c',c)
        #chipertext <<= 8
        chipertext += chr(E(ord(c), public))
    print('texto cifrado', chipertext)
    return chipertext
 
#Aqui utilizamos el mensaje y la llave privada
#para poder descifrar el mensaje, se recorre letra por letra
#Convertimos cada letra en su numero correspondiente a ASCII 
def decifrar(c, private):
    mensaje = ''
    for i in c:
        mensaje += chr(D(ord(i), private))
    return mensaje

#Codigo visto en ejemplo de clase
def get_coprime(N):
    coprimes = []
    for number in range(1, N+1):
        list_commons = []
        for i in range(1, min(number, N)+1):
            if number % i == N % i == 0:
                list_commons.append(i)
        if (len(list_commons) <= 1):
            coprimes.append(number)
    return coprimes

#Codigo visto en ejemplo de clase
def get_e(list_1, list_2):
    list_e = []
    for element in list_1:
        if (element in list_2 and element > 1):
            list_e.append(element)
    return list_e

# Fin de codigo extraido

#Gerera llave a apattir del largo
#y la escribe en los archivos
def arch_key(size, name):
    (publica, privada) = key_gen(size)
    pub = open(name+'pub.key', 'w')
    priv = open(name+'priv.key', 'w')
    for i in range(len(publica)):
        pub.write(str(publica[i])+'\n')
        priv.write(str(privada[i])+'\n')
    return

#Lee la llave de los archivos
def get_key(archivo):
    f = open(archivo, 'r')
    e = int(f.readline())
    n = int(f.readline())
    return (e, n)

#ESte genera el P, Q  y genera el E y D
def key_gen(size):
    p = getPrime(5,randfunc=get_random_bytes)
    print(p)
    q = getPrime(5,randfunc=get_random_bytes)
    print(q)
    n = p * q
    phin = (p-1) * (q-1)
    d = -1
    e = 0
    while d == -1:
        while True:
            e = choice(get_e(get_coprime(n), get_coprime(phin)))
            if math.gcd(phin, e) == 1:
                break
        d = MMI(e, phin)
    return ((e, n), (d, n))