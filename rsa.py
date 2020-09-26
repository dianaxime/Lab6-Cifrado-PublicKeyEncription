#!/usr/bin/python
from sys import argv
# from potmod import potmod
# from gcd import gcd, egcd
# from randprime import rprime, pickone, inversa
import math
from random import choice
# from Crypto import *
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

# Codigo extraido de http://pastebin.com/ypg2PXt2
# Convierte un string en un numero
def msg2num(s):
    n = 0
    for c in s:
        n <<= 8
        n += ord(c)
    return n

# Convierte un numero en un string
def num2msg(n):
    s = []
    while n > 0:
        s.insert(0, chr(n & 255))
        n >>= 8
    return ''.join(s)

def cifrar(m, public):
    print('mensaje',m)
    chipertext = ''
    for c in m:
        print('c',c)
        #chipertext <<= 8
        chipertext += chr(E(ord(c), public))
    print('texto cifrado', chipertext)
    return chipertext
 
def decifrar(c, private):
    mensaje = ''
    for i in c:
        mensaje += chr(D(ord(i), private))
    return mensaje


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


def get_e(list_1, list_2):
    list_e = []
    for element in list_1:
        if (element in list_2 and element > 1):
            list_e.append(element)
    return list_e

# Fin de codigo extraido

def arch_key(size, name):
    (publica, privada) = key_gen(size)
    pub = open(name+'pub.key', 'w')
    priv = open(name+'priv.key', 'w')
    for i in range(len(publica)):
        pub.write(str(publica[i])+'\n')
        priv.write(str(privada[i])+'\n')
    return

def get_key(archivo):
    f = open(archivo, 'r')
    e = int(f.readline())
    n = int(f.readline())
    return (e, n)

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