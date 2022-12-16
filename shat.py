from code_cesar import cesar_code
from code_hill import hill_code
from code_vigenere import vig_code
from code_hamming import hamming
print("¿Qué desea hacer?")
print("1. Enviar un mensaje")
print("2. Recibir un mensaje")
opción=input("Acción a realizar:")
op=int(opción)

if op==1:
    print("Elija el método de cifrado")
    print("1. Cifrado Cesar")
    print("2. Cifrado Hill")
    print("3. Cifrado Vigenere")
    opcion1=input("Ingrese su opción de cifrado:")
    op1=int(opcion1)

if op==2:
        print("Elija el método de decifrado")
        print("1. Cifrado Cesar")
        print("2. Cifrado Hill")
        print("3. Cifrado Vigenere")
        opcion2=input("Ingrese su opción de decifrado:")
        op2=int(opcion2)
    
if op1==1:
        mensaje=input("Ingrese su mensaje a enviar:")
        codificado=cesar_code(mensaje)
        codificado1=hamming(codificado)
        print(codificado)
        print("El mensaje codificado es:",codificado1)

if op1==2:
        mensaje=input("Ingrese su mensaje a enviar:")
        codificado=hill_code(mensaje)
        codificado1=hamming(codificado)
        print(codificado)
        print("El mensaje codificado es:",codificado1)

if op1==3:
        mensaje=input("Ingrese su mensaje a enviar:")
        codificado=vig_code(mensaje)
        codificado1=hamming(codificado)
        print(codificado)
        print("El mensaje codificado es:",codificado1)
