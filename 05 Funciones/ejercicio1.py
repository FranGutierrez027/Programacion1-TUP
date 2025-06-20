#Definicion de funciones


def obtener_resto (num1,num2):
    return num1- num2 * (num1//num2)

def es_multiplo(x,y):
    return obtener_resto (x,y) == 0

def sumatoria_divisores_propios(numero):
    sumatoria = 0
    for i  in range (1, (numero//2)+1)
        if es_multiplo(numero, i):
            sumatoria += i
    return sumatoria

def es_perfecto(numero):
    return sumatoria_divisores_propios(numero) == numero

#Programa principal

