
def hamming(palabra):
    import math
    from operator import xor
    codificado=''
    residuo=int
    aux=int
    d8=int
    d7=int
    d6=int
    d5=int
    d6=int
    d4=int
    d3=int
    d2=int
    d1=int
    p1=int
    p2=int
    p3=int
    p4=int

    for i in palabra:

        aux=ord(i)

        d8=aux%2
        residuo=math.trunc((aux-d8)/2)
        d7=math.trunc(residuo%2)
        residuo=math.trunc((residuo-d7)/2)
        d6=math.trunc(residuo%2)
        residuo=math.trunc((residuo-d6)/2)
        d5=math.trunc(residuo%2)
        residuo=math.trunc((residuo-d5)/2)
        d4=math.trunc(residuo%2)
        residuo=math.trunc((residuo-d4)/2)
        d3=math.trunc(residuo%2)
        residuo=math.trunc((residuo-d3)/2)
        d2=math.trunc(residuo%2)
        residuo=math.trunc((residuo-d2)/2)
        d1=residuo

        p1=xor(d1,d2)
        p1=xor(p1,d4)
        p1=xor(p1,d5)
        p1=xor(p1,d7)
        p2=xor(d1,d3)
        p2=xor(p2,d4)
        p2=xor(p2,d6)
        p2=xor(p2,d7)
        p3=xor(d2,d3)
        p3=xor(p3,d4)
        p3=xor(p3,d8)
        p4=xor(d5,d6)
        p4=xor(p4,d7)
        p4=xor(p4,d8)

        codificado=codificado+str(p1)+str(p2)+str(d1)+str(p3)+str(d2)+str(d3)+str(d4)+str(p4)+str(d5)+str(d6)+str(d7)+str(d8)
        
    return codificado


