#for numero in range(101):
#    print(numero)

#numero = int(input('Ingresa un numero: '))

#contador = 0

#while numero > 0:
   # contador += 1
 #   numero = numero // 10
    
#print(f'El número tiene {contador} dígitos')

#num1 = int(input('Ingresa el primer numero'))
#num2 = int(input('Ingresa el segundo numero'))

#acumulador = 0

#if num1 > num2:
     # Paso 1: Guarda el valor de num1 en temp
#    temp = num1

    # Paso 2: Asigna el valor de num2 a num1
#    num1 = num2

    # Paso 3: Asigna el valor guardado en temp a num2
#    num2 = temp


#for i in range(num1 + 1, num2 ):
#    acumulador += i 

#print(f'El resultado de la suma de los numeros entre {num1} y {num2} es igual a: {acumulador}')

#suma = 0 

#numero = int(input('Ingresa el numero que quieres sumar.'))

#while numero != 0:
#    suma += numero
#   print(f'Luego de ingresar {numero} el nuevo total es de {suma}.')
#    numero = int(input('Ingresa un nuevo numero'))

#print(f'Elejiste el numero 0. Dejamos de contar. El resultado total fue de {suma}')

#import random

#numero_secreto = random.randint(0,9)

#contadorIntentos = 0

#eleccion = -1

#while eleccion != numero_secreto:
#    eleccion = int(input('Ingresa el numero que creas que es el correcto: '))
#    contadorIntentos += 1
#    print('Ingresaste el numero INCORRECTO. Intenta de vuelta! ')

#print(f'Pudiste adivinar el numero solo necesitaste {contadorIntentos} intentos.')

#for i in range (100, -2, -2):
#    print (i)

#num1 = int(input('Ingresa un numero: '))

#suma = 0

#for i in range (0, num1 + 1):
#    print(f'El total actual es: {suma}')
#    suma += i
#    print(f'Habiendo sumado {i} el total ahora es {suma}')
#print(f'La suma total es: {suma}')

# -----------------------------------------------------------------
# PARTE 1: PREPARACIÓN Y CONFIGURACIÓN
# -----------------------------------------------------------------

# Nota del ejercicio: "preparado para procesar 100 números con un solo cambio"
# Por eso, usamos una variable para la cantidad total.
# Para probar, puedes usar un número pequeño como 5 o 10.
total_numeros_a_procesar = 10 

# Inicializamos los contadores. Deben empezar en 0 antes de contar.
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

print(f"Este programa te pedirá que ingreses {total_numeros_a_procesar} números enteros.")
print("-" * 30) # Imprime una línea para separar

# -----------------------------------------------------------------
# PARTE 2: BUCLE PARA PROCESAR LOS NÚMEROS
# -----------------------------------------------------------------

# Usamos un bucle 'for' con 'range()' para repetir el proceso la cantidad exacta de veces.
# La variable 'i' irá tomando valores desde 0 hasta (total_numeros_a_procesar - 1).
# Usamos 'i + 1' en el mensaje para que el usuario vea "Número 1", "Número 2", etc.
for i in range(total_numeros_a_procesar):
  
    # Pedimos el número al usuario y lo convertimos a entero (int)
    texto_ingresado = input(f"Ingresa el número {i + 1}/{total_numeros_a_procesar}: ")
    numero = int(texto_ingresado)
    
    # --- ANÁLISIS DEL NÚMERO ---
    
    # Chequeo 1: ¿Es positivo o negativo?
    # Un número es positivo si es mayor que 0.
    # Un número es negativo si es menor que 0.
    # El cero no es ni positivo ni negativo, por lo que no entra en ninguna de estas condiciones.
    if numero > 0:
        contador_positivos += 1  # Es lo mismo que: contador_positivos = contador_positivos + 1
    elif numero < 0:
        contador_negativos += 1  # Es lo mismo que: contador_negativos = contador_negativos + 1

    # Chequeo 2: ¿Es par o impar?
    # Usamos el operador módulo (%) que nos da el resto de una división.
    # Si el resto de dividir por 2 es 0, el número es par.
    # De lo contrario, es impar.
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

# -----------------------------------------------------------------
# PARTE 3: MUESTRA DE RESULTADOS
# -----------------------------------------------------------------

# Esta parte del código se ejecuta UNA SOLA VEZ, después de que el bucle 'for' ha terminado.
print("\n" + "=" * 30) # Salto de línea (\n) y separador para el resultado
print("      ANÁLISIS COMPLETO")
print("=" * 30)
print(f"Cantidad de números pares:    {contador_pares}")
print(f"Cantidad de números impares:  {contador_impares}")
print(f"Cantidad de números positivos: {contador_positivos}")
print(f"Cantidad de números negativos: {contador_negativos}")
print("=" * 30)