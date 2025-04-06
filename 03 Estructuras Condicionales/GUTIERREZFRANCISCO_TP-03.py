##1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#MayorEdad = 18

#Edad = int(input('Cual es tu edad?'))

#if Edad >= 18:
   # print(f'Ya que tienes {Edad}, eres mayor de edad')

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

#Nota = int(input("Cual es tu nota?"))

#if Nota >= 6:
#    print(f'Aprobado')
#else:
#    print(f'Desaprobado')

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

#numero1 = int(input('Ingrese el primer numero'))
#numero2 = int(input('Ingrese el segundo numero'))

#if (numero1 % 2) == 0 and (numero2 % 2) == 0:
#    print(f'Los numeros {numero2} y {numero1} son pares')
#else:
#    print("Ingrese un numero par porfavor")
                    
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

#Edad = int(input('Ingrese su edad'))

#if Edad < 12:
#    print(f'Eres un Nene')
#elif Edad >= 12 and Edad < 18:
#    print(f'Eres un adolescente')
#elif Edad >= 18 and Edad < 30:
#    print(f'Eres un adulto joven')
#elif Edad > 30:
#    print(f"Eres un adulto")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

#password = input('Ingrese su password')

#if len(password) >= 8 and len(password) <= 14:
#    print("Ha ingresado una contraseña correcta")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

#from statistics import mode, median, mean
#import random

# Generar lista de 50 números aleatorios del 1 al 100
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular los valores estadísticos
#media = mean(numeros_aleatorios)
#mediana = median(numeros_aleatorios)
#moda = mode(numeros_aleatorios)

# Mostrar los valores calculados
#print(f"Lista: {numeros_aleatorios}")
#print(f"Media: {media}")
#print(f"Mediana: {mediana}")
#print(f"Moda: {moda}")

# Comparar y determinar el sesgo
#if media > mediana and mediana > moda:
#    print('Hay sesgo positivo')
#elif media < mediana and mediana < moda:
#    print('Hay sesgo negativo')
#elif media == mediana == moda:
#    print('No hay sesgo')
#else:
#    print('La distribución no presenta un sesgo claramente definido')

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#frase = input('Ingrese una palabra')

#if frase[-1].lower() in "aeiou":
#    frase += '!'
#print (frase)

#Actividad 8

nombre = input('Ingrese su nombre')
opcion = int(input('Ingrese la opcion que quiera'))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print(f'la opcion ingresada no es correcta. Ingrese 1, 2 o 3')

#actividad 9 


magnitud = float(input("Ingresa la magnitud del terremoto: "))


if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

#actividad 10 

# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Función para determinar la estación
def obtener_estacion(hemisferio, mes, dia):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        return "Fecha inválida"

    return estacion_norte if hemisferio == "N" else estacion_sur

# Imprimir la estación
estacion = obtener_estacion(hemisferio, mes, dia)
print("Te encuentras en:", estacion)
