#Actividad 1 

def imprimir_hola_mundo():
    print('Hola Mundo!')

imprimir_hola_mundo()

#Actividad 2 

def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

saludar_usuario('Francisco')

#Actividad 3 

def informacion_personal(nombre,apellido,edad,residencia):
    print(f'Soy {nombre}{apellido}, tengo {edad} anios y vivo en {residencia}')

nombre = input('Ingresa tu nombre')
apellido = input('Ingresa tu apellido')
edad = input('Ingresa tu edad')
residencia = input('Donde vives?')

informacion_personal(nombre,apellido,edad,residencia)

#Actividad 4 

import math

def calcular_area_circulo(radio):
    return 2*math.pi*radio**2

def calcular_perimetro_circulo(radio):
    return 2*math.pi*radio

radio = float(input('Ingresa el radio del circulo: '))

area = calcular_area_circulo(radio)
perimetro= calcular_perimetro_circulo(radio)

print(f'El area del circulo es {area}')
print(f'El perimetro del circulo es {perimetro}')

#Actividad 5

def segundos_a_horas(segundos):
    return  segundos / 3600

segundos_ingresados = int(input('Ingresa la cantidad de segundos: '))

horas = segundos_a_horas(segundos_ingresados)

print(f'Los {segundos_ingresados} segundos que ingresaste, equivalen a {horas} horas.')

#Actividad 6

def tabla_multiplicar(numero):
    for i in range (1,10):
        print(f'{numero} x {i} = {numero * i}')

numero = int(input('Ingresa un numero para poder ver si tabla de multiplicar'))

tabla_multiplicar(numero)

#Actividad 7 

def operaciones_basicas (a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = 'No se puede dividir por 0 '
    return (suma,resta,multiplicacion,division)

a = float(input('Ingresa el primer numero: '))
b = float(input('Ingresa el segundo numero: '))

resultados = operaciones_basicas (a,b)

print(f'Suma: {resultados[0]}')
print(f'Resta: {resultados[1]}')
print(f'Multiplicacion: {resultados[2]}')
print(f'Division: {resultados[3]}')
    

#Actividad 8 

def calcular_imc(peso,altura):
    return peso / (altura ** 2)

peso = float(input('Ingresa tu peso en kilogramos: '))
altura = float(input('Ingresa tu altura en metros: '))

imc = calcular_imc (peso,altura)

print(f'Tu indice de masa corporal (IMC) es : {imc}')


#Actividad 9 

def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5) + 32)

celsius = float(input('Ingrese temperatura en celsisus'))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f'Los {celsius} grados celsisus ingresados equivalen a {fahrenheit} grados fahrenheit.')

#Actividad 10 

def calcular_promedio (a,b,c):
    return (a + b + c) / 3

a = float(input('Ingresa el primer numero'))
b = float(input('Ingresa el segundo numero'))
c = float(input('Ingresa el tercer numero'))

promedio = calcular_promedio(a,b,c)

print(f'El promedio de los numeros {a},{b} y {c} es igual a {promedio}')