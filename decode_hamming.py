from operator import xor

aux=int
p1=int
p2=int
p3=int
p4=int
e1=int
e2=int
e3=int
e4=int
er=int
correlativo=int

def separacion(mensaje):
    decode=''
    cantidad=mensaje.count('')
    cantidad1=cantidad-1
    caracteres=int(cantidad1/12)

    for i in range(caracteres):
        a=12*i-11
        b=12*i
        for j in range(a,b):
            decode=decode+mensaje[j]  
        return decode
        decode=''